"""Assemble the web edition page from body.html, body_abstract.html, body_bib.html. Usage: python3 assemble.py out.html"""
import sys, re
from bs4 import BeautifulSoup
out = sys.argv[1]
body = open('body.html').read(); abstract = open('body_abstract.html').read(); bib = open('body_bib.html').read()
soup = BeautifulSoup(body, 'html.parser')
# figures: wrap tables in scroll containers
for t in soup.find_all('table'):
    w = soup.new_tag('div', attrs={'class': 'tablewrap'}); t.wrap(w)
# build table of contents from top-level sections
toc = []
for sec in soup.find_all('section', recursive=False):
    h = sec.find(['h1']);
    if not h: continue
    sid = sec.get('id') or ''
    claim = sec.find('p', class_='claim', recursive=False)
    toc.append((sid, h.get_text(' ', strip=True), claim.get_text(' ', strip=True) if claim else ''))
toc_html = ''.join('<li><a href="#%s">%s</a></li>' % (i, re.sub(r'^\d+\s*', '', t)) for i, t, c in toc if i)
html = r'''<title>The Macroeconomic Limits of AI Compute</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;600;700&family=IBM+Plex+Serif:ital,wght@0,400;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: a paper you can scan. Left rail of section titles; one reading column; claims and In-brief always visible, detail folds away. */
:root{
  --bg:#F7F9FC; --paper:#FFFFFF; --ink:#1B2233; --muted:#55627A; --navy:#1E2761; --accent:#2E6DB4; --line:#D7E0EC; --tint:#EEF3FA; --warm:#B85042;
  --f-display:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif; --f-body:"IBM Plex Serif",Georgia,"Times New Roman",serif; --f-mono:"IBM Plex Mono",ui-monospace,Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--bg:#0F1522;--paper:#151D2E;--ink:#E6EBF3;--muted:#A5B1C6;--navy:#C7D5F2;--accent:#7FB0EA;--line:#2A3650;--tint:#1B2740;--warm:#E39A8E;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#0F1522;--paper:#151D2E;--ink:#E6EBF3;--muted:#A5B1C6;--navy:#C7D5F2;--accent:#7FB0EA;--line:#2A3650;--tint:#1B2740;--warm:#E39A8E;color-scheme:dark}
body{background:var(--bg);color:var(--ink);font-family:var(--f-body);font-size:17px;line-height:1.65}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 64px;display:grid;grid-template-columns:250px minmax(0,1fr);gap:40px}
@media (max-width:900px){.wrap{grid-template-columns:minmax(0,1fr)}.rail{display:none}}
.rail{position:sticky;top:calc(env(safe-area-inset-top,0px) + 16px);align-self:start;max-height:calc(100vh - 32px);overflow:auto;font-family:var(--f-display);font-size:13.5px;line-height:1.35}
.rail h4{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 10px}
.rail ol{list-style:none;padding:0;margin:0;display:grid;gap:6px}
.rail a{color:var(--navy);text-decoration:none}.rail a:hover{color:var(--accent);text-decoration:underline}
main{min-width:0;background:var(--paper);border:1px solid var(--line);border-radius:6px;padding:clamp(18px,4vw,48px)}
.eyebrow{font-family:var(--f-mono);font-size:12.5px;letter-spacing:.06em;color:var(--accent);text-transform:uppercase}
h1.title{font-family:var(--f-display);font-size:clamp(28px,4.4vw,44px);line-height:1.12;color:var(--navy);margin:.3em 0 .25em;text-wrap:balance}
.sub{font-family:var(--f-display);color:var(--muted);font-size:17px;margin:0 0 14px}
.byline{font-family:var(--f-display);font-size:14px;color:var(--muted);margin-bottom:24px}
.byline b{color:var(--ink)}
.stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:8px 0 28px}
@media (max-width:640px){.stats{grid-template-columns:repeat(2,minmax(0,1fr))}}
.stat{border-top:3px solid var(--navy);padding-top:8px}
.stat .n{font-family:var(--f-display);font-weight:700;font-size:clamp(22px,3vw,30px);color:var(--navy);font-variant-numeric:tabular-nums}
.stat .l{font-family:var(--f-display);font-size:13px;color:var(--muted);line-height:1.35}
.stat.gap{border-color:var(--warm)}.stat.gap .n{color:var(--warm)}
.controls{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 20px;font-family:var(--f-display)}
.controls button{font:600 13px var(--f-display);color:var(--navy);background:var(--tint);border:1px solid var(--line);border-radius:4px;padding:7px 12px;cursor:pointer}
.controls button:focus-visible,summary:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.abstract{background:var(--tint);border-left:4px solid var(--navy);padding:14px 18px 6px;margin:0 0 28px;border-radius:0 4px 4px 0}
.abstract h2{font-family:var(--f-display);font-size:13px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:0 0 6px}
.abstract ul{padding-left:20px;margin:0}.abstract li p{margin:.15em 0 .45em}
section{margin:0}
section h1{font-family:var(--f-display);font-size:clamp(22px,2.6vw,28px);color:var(--navy);line-height:1.2;margin:2.2em 0 .25em;padding-bottom:.25em;border-bottom:2px solid var(--line);text-wrap:balance}
section h2{font-family:var(--f-display);font-size:20px;color:var(--navy);margin:1.6em 0 .2em;text-wrap:balance}
section h3{font-family:var(--f-display);font-size:17px;color:var(--accent);margin:1.3em 0 .2em}
.header-section-number{color:var(--accent);margin-right:.45em}
p.claim{font-family:var(--f-display);font-size:18px;line-height:1.45;color:var(--accent);font-style:italic;margin:.2em 0 .9em;max-width:65ch}
.inbrief{background:var(--tint);border:1px solid var(--line);border-radius:4px;padding:10px 16px 4px;margin:0 0 1em;max-width:70ch}
.inbrief-h{font-family:var(--f-display);font-weight:700;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--navy)}
.inbrief ul{margin:.3em 0 .5em;padding-left:20px}.inbrief li{margin:.15em 0}
details.deeper{margin:.2em 0 1.2em}
details.deeper>summary{display:inline-flex;align-items:center;gap:6px;cursor:pointer;font:600 13.5px var(--f-display);color:var(--accent);list-style:none;padding:5px 10px;border:1px solid var(--line);border-radius:4px;background:var(--paper)}
details.deeper>summary::-webkit-details-marker{display:none}
details.deeper>summary::before{content:"+";font-weight:700}
details.deeper[open]>summary::before{content:"\2212"}
details.deeper[open]>summary{margin-bottom:.6em}
main p{max-width:70ch}
strong{color:var(--navy)}
a{color:var(--accent)}a.cite{text-decoration:none;font-family:var(--f-mono);font-size:.82em}
figure{margin:1.2em 0;max-width:100%}figure img{background:#fff;border:1px solid var(--line);border-radius:4px;padding:6px;max-width:100%;height:auto}
figcaption{font-family:var(--f-display);font-size:14px;color:var(--muted);margin-top:6px;max-width:70ch}
.tablewrap{overflow-x:auto;margin:1em 0;border:1px solid var(--line);border-radius:4px}
table{border-collapse:collapse;font-family:var(--f-display);font-size:13.5px;line-height:1.4;width:100%}
caption{caption-side:top;text-align:left;font-weight:600;color:var(--navy);padding:8px 10px}
th,td{padding:6px 10px;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}
thead th,tr.header th{background:var(--tint);color:var(--navy)}
tbody tr:nth-child(even) td{background:color-mix(in srgb,var(--tint) 45%,transparent)}
math{font-size:1.02em}
ol.bib{font-family:var(--f-display);font-size:13.5px;line-height:1.45;padding-left:0;list-style:none}
ol.bib li{margin:.4em 0;overflow-wrap:anywhere}.bnum{font-family:var(--f-mono);color:var(--muted);margin-right:4px}
blockquote{margin:1em 0;padding:10px 16px;background:var(--tint);border-radius:4px;border:1px solid var(--line)}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
</style>
<div class="wrap">
<nav class="rail" aria-label="Sections"><h4>The argument</h4><ol>%TOC%</ol></nav>
<main>
<div class="eyebrow">Version 28 &middot; 29 October 2026 &middot; after the third-quarter earnings</div>
<h1 class="title">The Macroeconomic Limits of AI Compute</h1>
<p class="sub">A Fermi model of what the AI build-out costs to carry, and how fast revenue must grow to pay for it</p>
<div class="byline"><b>Desmond Fitzpatrick, Ph.D.</b> &middot; Founder, Nvara.ai &middot; Retired, IBM Systems &middot; ORCID 0009-0001-0534-2793 &middot; desmond.fitzpatrick@nvara.ai</div>
<div class="stats">
<div class="stat"><div class="n">$780B</div><div class="l">Big-5 spending on AI data centers in 2026</div></div>
<div class="stat"><div class="n">$725B</div><div class="l">yearly cost to carry the build-out by 2030, even if spending stays flat</div></div>
<div class="stat"><div class="n">$179B</div><div class="l">AI revenue in 2026; it must grow ~49% a year to cover the cost</div></div>
<div class="stat gap"><div class="n">~$260B</div><div class="l">most likely shortfall in 2030; overturned if 2028 AI revenue tops $400B</div></div>
</div>
<div class="controls"><button type="button" id="openall">Open every "Dig deeper"</button><button type="button" id="closeall">Close them all</button></div>
<div class="abstract"><h2>The paper in eleven points</h2>%ABSTRACT%</div>
%BODY%
<section id="references"><h1>References</h1>%BIB%</section>
<p class="byline" style="margin-top:2em">Paper (PDF), model and every input: <a href="https://doi.org/10.5281/zenodo.23406475">doi.org/10.5281/zenodo.23406475</a> &middot; <a href="https://github.com/desfitz/ai-compute-limits">github.com/desfitz/ai-compute-limits</a> &middot; <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7620359">SSRN</a> &middot; <a href="https://datademocracy.substack.com/p/the-macroeconomic-limits-of-ai-compute">Data Democracy</a></p>
</main></div>
<script>
document.getElementById('openall').addEventListener('click',()=>document.querySelectorAll('details.deeper').forEach(d=>d.open=true));
document.getElementById('closeall').addEventListener('click',()=>document.querySelectorAll('details.deeper').forEach(d=>d.open=false));
// opening a link into folded text unfolds it
function reveal(){const id=decodeURIComponent(location.hash.slice(1));if(!id)return;const el=document.getElementById(id);if(!el)return;let p=el.parentElement;while(p){if(p.tagName==='DETAILS')p.open=true;p=p.parentElement}el.scrollIntoView()}
window.addEventListener('hashchange',reveal);document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#"]');if(a)setTimeout(reveal,0)});
</script>'''
html = html.replace('%TOC%', toc_html).replace('%ABSTRACT%', abstract).replace('%BODY%', str(soup)).replace('%BIB%', bib)
open(out, 'w').write(html)
print('written', len(html), 'toc', len(toc))
