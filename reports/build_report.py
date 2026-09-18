#!/usr/bin/env python3
"""Deterministic renderer: reports/data/<board>.json -> reports/<board>-job-search.html.

No AI involvement in HTML authoring. See reports/report_schema.md for the JSON schema.

Usage:
    python3 reports/build_report.py <board>       # e.g. "builtin"
    python3 reports/build_report.py --all         # regenerate every reports/data/*.json
"""
import json
import sys
from pathlib import Path

REPORTS_DIR = Path(__file__).resolve().parent
DATA_DIR = REPORTS_DIR / "data"

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title_tag}</title>
<style>
:root{{color-scheme:light dark;--bg:#f4f6f8;--panel:#fff;--ink:#15202b;--muted:#64748b;--line:#dbe2ea;--blue:#0969da;--soft:#f8fafc;--red:#b42318;--green:#18794e}}
@media(prefers-color-scheme:dark){{:root{{--bg:#0d1117;--panel:#161b22;--ink:#e6edf3;--muted:#9da7b3;--line:#30363d;--blue:#58a6ff;--soft:#0d1117;--red:#ff7b72;--green:#56d38b}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,"Segoe UI",sans-serif}}a{{color:var(--blue)}}
main{{width:min(1500px,calc(100% - 32px));margin:auto}}header{{padding:52px 0 28px}}.eyebrow{{color:var(--blue);font-size:12px;font-weight:800;letter-spacing:.13em;text-transform:uppercase}}
h1{{font-size:clamp(30px,5vw,52px);line-height:1.05;margin:10px 0}}.lede,.count,.method{{color:var(--muted)}}.latest{{font-weight:700;color:var(--blue);margin:8px 0 0}}
.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin:28px 0}}.stat,.notes,.table-shell,.panel{{background:var(--panel);border:1px solid var(--line);border-radius:13px}}
.stat{{padding:16px}}.stat b{{display:block;font-size:26px}}.stat span{{color:var(--muted);font-size:13px}}.controls{{display:grid;grid-template-columns:1fr repeat(3,190px);gap:10px;position:sticky;top:0;padding:12px 0;background:var(--bg)}}
input,select{{padding:10px 12px;border:1px solid var(--line);border-radius:8px;background:var(--panel);color:var(--ink);font:inherit}}.table-shell{{overflow:auto}}
table{{border-collapse:collapse;width:100%;min-width:1000px}}th,td{{padding:13px 12px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}}
th{{background:var(--soft);color:var(--muted);font-size:11px;text-transform:uppercase;cursor:pointer}}.score{{font-size:18px;font-weight:800}}.high{{color:var(--green)}}.low{{color:#b77900}}
.pill{{display:inline-block;padding:3px 8px;border-radius:99px;background:var(--soft);border:1px solid var(--line);font-size:11px;font-weight:700}}.job,.company,.posting{{font-weight:700}}
.empty{{text-align:center;padding:34px;color:var(--muted)}}.panel{{padding:22px;margin:24px 0}}.notes{{padding:22px;margin:28px 0 70px}}.notes h2,.panel h2{{margin-top:0}}.notes li+li,.panel li+li{{margin-top:7px}}
.reason{{color:var(--red)}}@media(max-width:800px){{.stats{{grid-template-columns:1fr 1fr}}.controls{{position:static;grid-template-columns:1fr}}}}
</style>
</head>
<body><main>
<header>
  <div class="eyebrow">{eyebrow}</div>
  <h1>{title}</h1>
  <p class="lede">{lede}</p>
  <p class="latest">{latest_update}</p>
  <div class="stats">
{stats_html}
  </div>
</header>
<section>
  <div class="controls">
    <input id="q" type="search" placeholder="Search title, company, location or gap…">
    <select id="family"><option value="">All families</option><option>SRE</option><option>Platform</option><option>DevOps</option></select>
    <select id="location"><option value="">All locations</option></select>
    <select id="minimum"><option value="0">Any score</option><option value="8">8+ strong fit</option><option value="6">6+ plausible fit</option><option value="4">4+ stretch</option></select>
    <label class="pill"><input id="hideDone" type="checkbox" checked> Hide applied &amp; rejected</label>
  </div>
  <p class="count" id="count"></p>
  <div class="table-shell"><table>
    <thead><tr><th data-k="score">Score</th><th data-k="family">Family</th><th data-k="title">Job title</th><th data-k="company">Company</th><th data-k="location">Location / cadence</th><th>Salary</th><th>Biggest gap</th><th>Posting</th></tr></thead>
    <tbody id="rows"></tbody>
  </table></div>
</section>
{ineligible_html}{could_not_validate_html}{notes_html}{method_html}
</main>
<script>
const jobs = {rows_json};
const $=s=>document.querySelector(s),rowsEl=$("#rows");let key="score",dir=-1;
const esc=s=>String(s).replace(/[&<>"']/g,c=>({{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}}[c]));
function render(){{
  const q=$("#q").value.toLowerCase(),family=$("#family").value,location=$("#location").value.toLowerCase(),minimum=+$("#minimum").value,hideDone=$("#hideDone").checked;
  const list=jobs.filter(j=>(!hideDone||!/(applied|rejected)/i.test(j.status||""))&&(!family||j.family===family)&&(!location||(j.location||"").toLowerCase().includes(location))&&j.score>=minimum&&(!q||Object.values(j).join(" ").toLowerCase().includes(q))).sort((a,b)=>dir*(a[key]<b[key]?-1:a[key]>b[key]?1:0));
  rowsEl.innerHTML=list.length?list.map(j=>`<tr><td><span class="score ${{j.score>=8?"high":j.score<=4?"low":""}}">${{j.score}}/10</span></td><td><span class="pill">${{esc(j.family)}}</span></td><td class="job">${{esc(j.title)}}${{j.status?`<br><span class="pill">${{esc(j.status)}}</span>`:""}}</td><td class="company">${{esc(j.company)}}</td><td>${{esc(j.location||"")}}</td><td>${{esc(j.salary||"Not stated")}}</td><td>${{esc(j.gap||"")}}</td><td><a class="posting" href="${{esc(j.url)}}" target="_blank" rel="noopener">View ↗</a></td></tr>`).join(""):`<tr><td class="empty" colspan="8">No postings match the current filters.</td></tr>`;
  $("#count").textContent=`Showing ${{list.length}} of ${{jobs.length}} validated postings`;
}}
const locSel=$("#location");[...new Set(jobs.map(j=>j.location).filter(Boolean))].sort().forEach(loc=>{{const o=document.createElement("option");o.textContent=loc;locSel.append(o)}});
["q","family","location","minimum","hideDone"].forEach(id=>$("#"+id).addEventListener("input",render));
document.querySelectorAll("th[data-k]").forEach(th=>th.onclick=()=>{{const next=th.dataset.k;if(key===next)dir*=-1;else{{key=next;dir=key==="score"?-1:1}}render()}});
render();
</script>
</body>
</html>
"""


def esc(s):
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def render_stats(stats):
    if not stats:
        return "    <div class=\"stat\"><b>0</b><span>no data yet</span></div>"
    return "\n".join(
        f'    <div class="stat"><b>{esc(s["value"])}</b><span>{esc(s["label"])}</span></div>'
        for s in stats
    )


def render_ineligible(ineligible):
    if not ineligible:
        return ""
    rows = "\n".join(
        f'<tr><td><a href="{esc(i.get("url", "#"))}">{esc(i["title"])} — {esc(i["company"])}</a></td>'
        f'<td class="reason">{esc(i["reason"])}</td></tr>'
        for i in ineligible
    )
    return (
        '<section class="panel"><h2>Ineligible — not scored</h2><table>'
        "<thead><tr><th>Role — Company</th><th>Reason</th></tr></thead>"
        f"<tbody>{rows}</tbody></table></section>\n"
    )


def render_could_not_validate(items):
    if not items:
        return ""
    lis = "\n".join(f"<li>{esc(i)}</li>" for i in items)
    return f'<section class="panel"><h2>Could not validate</h2><ul>{lis}</ul></section>\n'


def render_notes(notes_sections):
    if not notes_sections:
        return ""
    blocks = []
    for section in notes_sections:
        lis = "\n".join(f"<li>{i}</li>" for i in section["items"])
        blocks.append(f'<h2>{esc(section["heading"])}</h2><ul>{lis}</ul>')
    return f'<aside class="notes">{"".join(blocks)}</aside>\n'


def render_method(method):
    if not method:
        return ""
    return f'<p class="method">{method}</p>\n'


def build(board):
    data_path = DATA_DIR / f"{board}.json"
    if not data_path.exists():
        print(f"no data file for '{board}' at {data_path}", file=sys.stderr)
        return False
    data = json.loads(data_path.read_text(encoding="utf-8"))

    rows = data.get("rows", [])
    html = TEMPLATE.format(
        title_tag=esc(f"{data['board']} job search — {data['run_date']}"),
        eyebrow=esc(data.get("eyebrow", data["board"])),
        title=esc(data.get("title", f"{data['board']} opportunities")),
        lede=esc(data.get("lede", "")),
        latest_update=esc(data.get("latest_update", f"Latest update: {data['run_date']}")),
        stats_html=render_stats(data.get("stats", [])),
        ineligible_html=render_ineligible(data.get("ineligible")),
        could_not_validate_html=render_could_not_validate(data.get("could_not_validate")),
        notes_html=render_notes(data.get("notes_sections")),
        method_html=render_method(data.get("method")),
        rows_json=json.dumps(rows, ensure_ascii=False).replace("</script>", "<\\/script>"),
    )

    out_path = REPORTS_DIR / f"{board}-job-search.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"wrote {out_path} ({len(rows)} rows)")
    return True


def rebuild_index():
    index_path = REPORTS_DIR / "index.html"
    if not index_path.exists():
        return
    text = index_path.read_text(encoding="utf-8")

    display_names = {
        "indeed": "Indeed",
        "linkedin": "LinkedIn",
        "builtin": "Built In",
        "jobbank": "Job Bank",
        "dice": "Dice",
        "eluta": "Eluta",
        "randstad": "Randstad",
        "remoteok": "RemoteOK",
        "sisystems": "S.i. Systems",
        "braintrust": "Braintrust",
        "wwr": "We Work Remotely",
        "glassdoor": "Glassdoor",
        "procom": "Procom",
        "roberthalf": "Robert Half",
    }
    boards = sorted(p.stem for p in DATA_DIR.glob("*.json"))
    entries = ",\n".join(
        f'      ["{display_names.get(b, b.title())}", "{b}-job-search.html"]' for b in boards
    )
    new_array = "const reports = [\n" + entries + "\n    ];"

    import re

    updated, count = re.subn(
        r"const reports = \[.*?\];",
        new_array.replace("\\", "\\\\"),
        text,
        count=1,
        flags=re.DOTALL,
    )
    if count:
        index_path.write_text(updated, encoding="utf-8")
        print(f"rebuilt reports/index.html nav ({len(boards)} boards)")


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    if argv[0] == "--all":
        ok = True
        for data_file in sorted(DATA_DIR.glob("*.json")):
            ok = build(data_file.stem) and ok
        rebuild_index()
        return 0 if ok else 1
    return 0 if build(argv[0]) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
