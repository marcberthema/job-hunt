#!/usr/bin/env python3
"""Resume Markdown -> print HTML -> PDF (Brave headless).
Styling follows resume/style_guide.md §3 (typography), §8 (2 pages), §11 (real text)."""
import io, os, re, subprocess, sys, html as H

CSS = """
@page { size: Letter; margin: 0.6in 0.65in; }
:root { --accent:#1a3c5e; --fg:#111; --muted:#444; --rule:#c9d4de; }
* { box-sizing:border-box; }
body { font-family:"Inter","Helvetica Neue",Helvetica,Arial,sans-serif;
       font-size:10pt; line-height:1.27; color:var(--fg); margin:0;
       -webkit-print-color-adjust:exact; print-color-adjust:exact; }
h1 { font-size:22pt; font-weight:700; color:var(--accent); letter-spacing:-.01em; margin:0 0 2pt; }
h2 { font-size:12.5pt; font-weight:700; color:var(--accent); margin:6pt 0 2.5pt;
     padding-bottom:2pt; border-bottom:1px solid var(--rule); }
h3 { font-size:10.5pt; font-weight:700; margin:6pt 0 0; page-break-after:avoid; }
p  { margin:0 0 3pt; }
.subtitle { font-size:11pt; font-weight:600; color:var(--muted); margin:0 0 4pt; }
.contact { font-size:9.2pt; color:var(--muted); margin:0 0 2pt; }
.contact a { color:var(--muted); text-decoration:none; }
.meta { font-size:9.3pt; color:var(--muted); margin:0 0 2.5pt; }
.meta em { color:var(--muted); }
ul { margin:0 0 3pt; padding-left:12pt; }
li { margin:0 0 1.1pt; page-break-inside:avoid; }
.keytech { font-size:9pt; color:var(--muted); margin:1pt 0 0; }
table { border-collapse:collapse; width:100%; margin:0 0 6pt; font-size:9.8pt; }
td { vertical-align:top; padding:1.8pt 6pt 1.8pt 0; border-bottom:1px solid #eef2f5; }
td:first-child { width:31%; font-weight:600; color:var(--fg); }
hr { display:none; }
.role { }
h3 + .meta { page-break-after:avoid; }
"""

INLINE = [
    (re.compile(r'\[([^\]]+)\]\(([^)]+)\)'), r'<a href="\2">\1</a>'),
    (re.compile(r'\*\*(.+?)\*\*'), r'<strong>\1</strong>'),
    (re.compile(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)'), r'<em>\1</em>'),
]

def inline(t):
    t = H.escape(t, quote=False)
    for rx, rep in INLINE:
        t = rx.sub(rep, t)
    return t

def convert(md):
    lines = md.split('\n')
    out, i, in_ul, first_h1 = [], 0, False, True
    def close_ul():
        nonlocal in_ul
        if in_ul: out.append('</ul>'); in_ul = False
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            close_ul(); i += 1; continue
        if ln.startswith('---') and set(ln.strip()) == {'-'}:
            close_ul(); i += 1; continue
        # table
        if ln.startswith('|') and i+1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i+1].strip()):
            close_ul(); i += 2; out.append('<table>')
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells) + '</tr>')
                i += 1
            out.append('</table>'); continue
        m = re.match(r'^(#{1,3})\s+(.*)$', ln)
        if m:
            close_ul(); lvl, txt = len(m.group(1)), inline(m.group(2))
            if lvl == 3: out.append(f'<div class="role"><h3>{txt}</h3>')
            else: out.append(f'<h{lvl}>{txt}</h{lvl}>')
            i += 1; continue
        if ln.lstrip().startswith('- '):
            if not in_ul: out.append('<ul>'); in_ul = True
            out.append(f'<li>{inline(ln.lstrip()[2:])}</li>'); i += 1; continue
        close_ul()
        # paragraph, honouring trailing "\" and double-space line breaks
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,3}\s|\||- |---)', lines[i].lstrip()):
            raw = lines[i]
            buf.append(inline(raw.rstrip().rstrip('\\')) + ('<br>' if raw.rstrip().endswith('\\') or raw.endswith('  ') else ' '))
            i += 1
        txt = ''.join(buf).strip()
        cls = ''
        if first_h1 and out and out[-1].startswith('<h1'): cls, first_h1 = ' class="subtitle"', False
        elif '@' in txt or 'linkedin' in txt.lower(): cls = ' class="contact"'
        elif txt.startswith('<strong>Montr') or 'Present' in txt or 'Présent' in txt or re.match(r'^<strong>[A-ZÉÀ]', txt) and '|' in txt: cls = ' class="meta"'
        elif txt.startswith('<strong>Key technologies') or txt.startswith('<strong>Technologies cl'): cls = ' class="keytech"'
        out.append(f'<p{cls}>{txt}</p>')
    close_ul()
    # close .role divs
    body = '\n'.join(out)
    body = re.sub(r'(<div class="role">)', lambda m: '</div>' + m.group(1), body, count=body.count('<div class="role">'))
    if body.startswith('</div>'): body = body[6:]
    return body + '</div>'

# French runs ~25% longer than English at identical content; a slightly tighter
# type scale keeps the FR edition inside the two-page limit (style_guide.md §8).
FR_CSS = """
@page { margin: 0.55in 0.6in; }
body { font-size:9.5pt; line-height:1.26; }
h1 { font-size:20pt; } h2 { font-size:12pt; margin:5.5pt 0 2pt; } h3 { font-size:10pt; }
li { margin:0 0 1.2pt; } p { margin:0 0 2.6pt; }
.keytech { font-size:8.6pt; } .meta { font-size:8.9pt; }
td { padding:1.5pt 6pt 1.5pt 0; } table { font-size:9.3pt; }
"""

def build(md_path, pdf_path, lang):
    md = io.open(md_path, encoding='utf-8').read()
    css = CSS + (FR_CSS if lang == 'fr' else '')
    doc = (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8">'
           f'<title>{os.path.basename(pdf_path)}</title><style>{css}</style></head>'
           f'<body>{convert(md)}</body></html>')
    tmp = pdf_path.replace('.pdf', '.print.html')
    io.open(tmp, 'w', encoding='utf-8').write(doc)
    subprocess.run(['brave', '--headless', '--disable-gpu', '--no-sandbox',
                    '--no-pdf-header-footer', f'--print-to-pdf={pdf_path}',
                    'file://' + os.path.abspath(tmp)], check=True,
                   capture_output=True, timeout=120)
    return tmp

if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    for lang in ('en', 'fr'):
        md = os.path.join(base, f'marc-berthelette-resume-{lang}.md')
        pdf = os.path.join(base, 'export', f'marc-berthelette-resume-{lang}.pdf')
        tmp = build(md, pdf, lang)
        print(f'{lang}: {pdf} ({os.path.getsize(pdf)} bytes)')
