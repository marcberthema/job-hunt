#!/usr/bin/env python3
"""Generic Markdown -> print HTML -> PDF (Brave headless), one file at a time.
Same visual standard as build_pdf.py / build_targeted_pdf.js (resume/style_guide.md).

Usage:
    python3 resume/md_to_pdf.py <input.md> [output.pdf] [--lang en|fr]

If output.pdf is omitted, it's derived from the input path (same name, .pdf extension).
Works for the base resume, tailored resumes, and cover letters alike — anything built
from the same heading/list/table/paragraph markdown conventions.
"""
import argparse
import io
import os
import re
import subprocess
import sys
import html as H

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

FR_CSS = """
@page { margin: 0.55in 0.6in; }
body { font-size:9.5pt; line-height:1.26; }
h1 { font-size:20pt; } h2 { font-size:12pt; margin:5.5pt 0 2pt; } h3 { font-size:10pt; }
li { margin:0 0 1.2pt; } p { margin:0 0 2.6pt; }
.keytech { font-size:8.6pt; } .meta { font-size:8.9pt; }
td { padding:1.5pt 6pt 1.5pt 0; } table { font-size:9.3pt; }
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
        if in_ul:
            out.append('</ul>')
            in_ul = False

    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            close_ul()
            i += 1
            continue
        if ln.startswith('---') and set(ln.strip()) == {'-'}:
            close_ul()
            i += 1
            continue
        if ln.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
            close_ul()
            i += 2
            out.append('<table>')
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells) + '</tr>')
                i += 1
            out.append('</table>')
            continue
        m = re.match(r'^(#{1,3})\s+(.*)$', ln)
        if m:
            close_ul()
            lvl, txt = len(m.group(1)), inline(m.group(2))
            if lvl == 3:
                out.append(f'<div class="role"><h3>{txt}</h3>')
            else:
                out.append(f'<h{lvl}>{txt}</h{lvl}>')
            i += 1
            continue
        if ln.lstrip().startswith('- '):
            if not in_ul:
                out.append('<ul>')
                in_ul = True
            out.append(f'<li>{inline(ln.lstrip()[2:])}</li>')
            i += 1
            continue
        close_ul()
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,3}\s|\||- |---)', lines[i].lstrip()):
            raw = lines[i]
            buf.append(inline(raw.rstrip().rstrip('\\')) + ('<br>' if raw.rstrip().endswith('\\') or raw.endswith('  ') else ' '))
            i += 1
        txt = ''.join(buf).strip()
        cls = ''
        if first_h1 and out and out[-1].startswith('<h1'):
            cls, first_h1 = ' class="subtitle"', False
        elif '@' in txt or 'linkedin' in txt.lower():
            cls = ' class="contact"'
        elif txt.startswith('<strong>Montr') or 'Present' in txt or 'Présent' in txt or (re.match(r'^<strong>[A-ZÉÀ]', txt) and '|' in txt):
            cls = ' class="meta"'
        elif txt.startswith('<strong>Key technologies') or txt.startswith('<strong>Technologies cl'):
            cls = ' class="keytech"'
        out.append(f'<p{cls}>{txt}</p>')
    close_ul()
    body = '\n'.join(out)
    body = re.sub(r'(<div class="role">)', lambda m: '</div>' + m.group(1), body, count=body.count('<div class="role">'))
    if body.startswith('</div>'):
        body = body[6:]
    return body + '</div>'


def build(md_path, pdf_path, lang='en', keep_html=False):
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
    if not keep_html:
        os.remove(tmp)
    return pdf_path


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('input', help='Source markdown file')
    ap.add_argument('output', nargs='?', help='Output PDF path (default: same name as input, .pdf)')
    ap.add_argument('--lang', choices=['en', 'fr'], default='en', help='Language (affects type scale for FR)')
    ap.add_argument('--keep-html', action='store_true', help='Keep the intermediate .print.html file')
    args = ap.parse_args()

    if not os.path.isfile(args.input):
        sys.exit(f'error: {args.input} not found')

    output = args.output or re.sub(r'\.md$', '.pdf', args.input)
    if not output.endswith('.pdf'):
        output += '.pdf'

    pdf = build(args.input, output, lang=args.lang, keep_html=args.keep_html)
    print(f'{pdf} ({os.path.getsize(pdf)} bytes)')


if __name__ == '__main__':
    main()
