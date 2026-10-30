"""Build the web edition of the paper: claims and In-brief visible, detail behind 'Dig deeper'.
Usage: python3 make_web.py paper.tex figures_png_dir out.html"""
import re, sys, subprocess, html
from bs4 import BeautifulSoup

tex, figdir, out = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(tex).read()
pre, body = s.split(r"\begin{document}", 1)
body = body.split(r"\end{document}")[0]

def balanced(text, start):
    """return index after the balanced {...} starting at text[start]=='{'"""
    d = 0
    for i in range(start, len(text)):
        if text[i] == '{' and text[i-1] != '\\': d += 1
        elif text[i] == '}' and text[i-1] != '\\':
            d -= 1
            if d == 0: return i + 1
    raise ValueError

def replace_macro(text, name, fn):
    out = []; i = 0; key = '\\' + name + '{'
    while True:
        j = text.find(key, i)
        if j < 0: out.append(text[i:]); break
        k = balanced(text, j + len(key) - 1)
        out.append(text[i:j]); out.append(fn(text[j + len(key):k - 1])); i = k
    return ''.join(out)

b = body
b = replace_macro(b, 'claim', lambda x: '\n\n\\begin{quote}CLAIMMARK ' + x + '\\end{quote}\n\n')
b = replace_macro(b, 'inbrief', lambda x: '\n\n\\begin{quote}INBRIEFMARK\n\\begin{itemize}' + x + '\\end{itemize}\\end{quote}\n\n')
b = replace_macro(b, 'figbox', lambda x: x)
b = replace_macro(b, 'lead', lambda x: '\\textbf{' + x + '}')
b = b.replace('\\verify', '')
b = re.sub(r'L\{([0-9.]+cm)\}', r'p{\1}', b)
b = re.sub(r'>\{[^{}]*\}p\{', 'p{', b)
b = re.sub(r'\\begingroup\\(small|footnotesize)', '', b).replace('\\endgroup', '')

def fix_xlt(m):
    blk=m.group(0)
    cap=re.search(r'\\caption\{((?:[^{}]|\{[^{}]*\})*)\}(\\label\{[^}]*\})?\\\\',blk)
    spec=re.match(r'\\begin\{xltabular\}\{\\textwidth\}\{((?:[^{}]|\{[^{}]*\})*)\}',blk).group(1)
    inner=blk[blk.index('}',blk.index(spec)+len(spec)-1)+1:blk.rindex('\\end{xltabular}')]
    inner=re.sub(r'\\caption\{(?:[^{}]|\{[^{}]*\})*\}(\\label\{[^}]*\})?\\\\','',inner,count=1)
    inner=re.sub(r'\\endfirsthead.*?\\endlastfoot','',inner,flags=re.S)
    head=('\\begin{table}\\caption{'+cap.group(1)+'}'+(cap.group(2) or '')) if cap else '\\begin{table}'
    return head+'\n\\begin{tabularx}{\\textwidth}{'+spec+'}'+inner+'\\end{tabularx}\\end{table}'
b = re.sub(r'\\begin\{xltabular\}.*?\\end\{xltabular\}', fix_xlt, b, flags=re.S)

b = re.sub(r'\\endfirsthead.*?\\endlastfoot', '', b, flags=re.S)
b = re.sub(r'\\resizebox\{\\textwidth\}\{!\}\{', r'\\begin{rbox}', b)
# resizebox wrappers: drop the opening; the closing brace after \end{tabular} -> remove
b = re.sub(r'\\begin\{rbox\}(\\begin\{tabular\}.*?\\end\{tabular\})\}', r'\1', b, flags=re.S)
b = re.sub(r'\\fcolorbox\{[^}]*\}\{[^}]*\}\{\\begin\{minipage\}\{[^}]*\}', r'\\begin{quote}', b)
b = b.replace('\\end{minipage}}', '\\end{quote}')
b = re.sub(r'\\includegraphics(\[[^\]]*\])?\{([^}]*)\.pdf\}', lambda m: '\\includegraphics{' + m.group(2) + '.png}', b)
b = re.sub(r'\\(maketitle|newpage|clearpage|vspace\*?\{[^}]*\}|hspace\*?\{[^}]*\}|dotfill|noindent|par)\b', '', b)

def fixtx(m):
    spec=m.group(1).replace('X','l')
    return '\\begin{tabular}{'+spec+'}'
b = re.sub(r'\\begin\{tabularx\}\{\\textwidth\}\{((?:[^{}]|\{[^{}]*\})*)\}', fixtx, b)
b = b.replace('\\end{tabularx}', '\\end{tabular}')
b = re.sub(r'\\(scriptsize|footnotesize|small|centering)\b', '', b)
b = re.sub(r'\\setlength\\itemsep\{[^}]*\}', '', b)
b = re.sub(r'\\multicolumn\{(\d+)\}\{p\{\\dimexpr[^}]*\}\}', r'\\multicolumn{\1}{l}', b)

abs_m = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', b, re.S)
abstract_tex = abs_m.group(1) if abs_m else ''
b = b.replace(abs_m.group(0), '') if abs_m else b
rg = b.find('Reading guide')
if rg > 0:
    st = b.rfind('\\begin{quote}', 0, rg); en = b.find('\\end{quote}', rg) + len('\\end{quote}')
    b = b[:st] + b[en:]
bib_m = re.search(r'\\begin\{thebibliography\}\{[^}]*\}(.*?)\\end\{thebibliography\}', b, re.S)
bibs = re.findall(r'\\bibitem\{([^}]*)\}(.*?)(?=\\bibitem\{|$)', bib_m.group(1), re.S) if bib_m else []
b = b.replace(bib_m.group(0), '') if bib_m else b
src = '\\documentclass{article}\n\\begin{document}\n' + b + '\n\\end{document}\n'
open('/tmp/web_src.tex', 'w').write(src)
r = subprocess.run(['pandoc', '/tmp/web_src.tex', '-f', 'latex', '-t', 'html5', '--mathml', '--section-divs',
                    '--wrap=none'], capture_output=True, text=True)
if r.returncode: print(r.stderr[:3000]); sys.exit(1)
soup = BeautifulSoup(r.stdout, 'html.parser')

for bq in soup.find_all('blockquote'):
    t = bq.get_text(' ', strip=True)
    if t.startswith('CLAIMMARK'):
        p = soup.new_tag('p', attrs={'class': 'claim'})
        inner = bq.find('p') or bq
        for c in list(inner.contents): p.append(c.extract() if hasattr(c, 'extract') else c)
        first = p.contents[0] if p.contents else None
        if isinstance(first, str): first.replace_with(first.replace('CLAIMMARK', '').lstrip())
        bq.replace_with(p)
    elif t.startswith('INBRIEFMARK'):
        d = soup.new_tag('div', attrs={'class': 'inbrief'})
        h = soup.new_tag('div', attrs={'class': 'inbrief-h'}); h.string = 'In brief'; d.append(h)
        ul = bq.find('ul')
        if ul: d.append(ul.extract())
        bq.replace_with(d)


def pandoc_frag(t):
    rr = subprocess.run(['pandoc','-f','latex','-t','html5','--mathml','--wrap=none'], input='\\documentclass{article}\\begin{document}'+t+'\\end{document}', capture_output=True, text=True)
    return rr.stdout
num = {k:i+1 for i,(k,_) in enumerate(bibs)}
for sp in soup.find_all('span', class_='citation'):
    keys = sp.get('data-cites','').split()
    links = []
    for k in keys:
        a = soup.new_tag('a', href='#bib-'+k.replace(':','-'), attrs={'class':'cite'}); a.string = str(num.get(k,'?')); links.append(a)
    sp.clear(); sp.append('[')
    for i,a in enumerate(links):
        if i: sp.append(', ')
        sp.append(a)
    sp.append(']')
# cross references from the LaTeX aux file
aux = open(tex.replace('.tex','.aux')).read() if __import__('os').path.exists(tex.replace('.tex','.aux')) else ''
labels = dict(re.findall(r'\\newlabel\{([^}]*)\}\{\{([^}]*)\}', aux))
for a in soup.find_all('a', href=True):
    h = a['href']
    if h.startswith('#') and h[1:] in labels and (a.string or '').strip().replace('.','').isdigit():
        a.string = labels[h[1:]]
bib_html = ''
for k,t in bibs:
    frag = BeautifulSoup(pandoc_frag(t.strip()), 'html.parser')
    inner = ''.join(str(x) for x in (frag.find('p').contents if frag.find('p') else frag.contents))
    bib_html += '<li id="bib-%s"><span class="bnum">[%d]</span> %s</li>\n' % (k.replace(':','-'), num[k], inner)
abstract_html = pandoc_frag(abstract_tex.replace('\\lead{','\\textbf{'))
asoup = BeautifulSoup(abstract_html,'html.parser')
for sp in asoup.find_all('span', class_='citation'):
    ks=sp.get('data-cites','').split(); sp.clear(); sp.append('['+', '.join(str(num.get(k,'?')) for k in ks)+']')
abstract_html=str(asoup)
open(out.replace('.html','_abstract.html'),'w').write(abstract_html)
open(out.replace('.html','_bib.html'),'w').write('<ol class="bib">'+bib_html+'</ol>')

tops=[x for x in soup.find_all('section', recursive=False)]
appendix_ids=set(); seen=False
for x in tops:
    if seen: appendix_ids.add(x.get('id'))
    h=x.find('h1')
    if h and 'Acknowledgments' in h.get_text(): seen=True
# wrap detail after heading + claim + inbrief into <details>
for sec in soup.find_all('section'):
    kids = [k for k in sec.children if getattr(k, 'name', None)]
    if not kids or kids[0].name not in ('h1', 'h2', 'h3'): continue
    keep = 1
    while keep < len(kids) and kids[keep].name in ('p', 'div') and set(kids[keep].get('class', [])) & {'claim', 'inbrief'}:
        keep += 1
    rest = [k for k in kids[keep:] if k.name != 'section']
    if not rest: continue
    top = sec
    while top.parent is not None and top.parent.name == 'section': top = top.parent
    if keep == 1 and top.get('id') not in appendix_ids: continue
    det = soup.new_tag('details', attrs={'class': 'deeper'})
    sm = soup.new_tag('summary'); sm.string = 'Dig deeper'; det.append(sm)
    rest[0].insert_before(det)
    for k in rest: det.append(k.extract())

body_html = str(soup)
open(out, 'w').write(body_html)
print('ok', len(body_html))
