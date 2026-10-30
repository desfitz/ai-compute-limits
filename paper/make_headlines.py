"""Build HEADLINES.md from paper.tex: section titles, the claim under each, In-brief points, and the headline of every paragraph/point. Usage: python3 make_headlines.py paper.tex > HEADLINES.md"""
import re, sys
s=open(sys.argv[1]).read(); s=s[s.index(r'\begin{document}'):]
def clean(t):
    t=re.sub(r'\\cite\{[^}]*\}','',t); t=re.sub(r'~\\ref\{[^}]*\}|\\ref\{[^}]*\}|\\pageref\{[^}]*\}|\\label\{[^}]*\}','',t)
    t=re.sub(r'\$\\sim\$','~',t); t=t.replace(r'\%','%').replace(r'\$','$').replace('---','-').replace('--','-').replace(r'\&','&')
    t=re.sub(r'\\(emph|textbf|textit|texttt|lead)\{([^{}]*)\}',r'\2',t); t=re.sub(r'\$([^$]*)\$',r'\1',t)
    t=re.sub(r'\\[a-zA-Z]+\*?','',t); t=t.replace('{','').replace('}','')
    return re.sub(r'\s+',' ',t).strip()
out=["# The paper in headlines (v28, 2026-10-30)","","Section titles, the one-line claim under each, the In-brief points, and the headline of every paragraph and point, in order.",""]
tok=re.compile(r'\\(section|subsection|subsubsection)\*?\{((?:[^{}]|\{[^{}]*\})*)\}|\\claim\{((?:[^{}]|\{[^{}]*\})*)\}|\\inbrief\{(.*?)\n\}|\\lead\{((?:[^{}]|\{[^{}]*\})*)\}|\\item \\textbf\{((?:[^{}]|\{[^{}]*\})*)\}',re.S)
for m in tok.finditer(s):
    if m.group(1):
        lvl={'section':'##','subsection':'###','subsubsection':'####'}[m.group(1)]; out+=["",f"{lvl} {clean(m.group(2))}"]
    elif m.group(3): out.append(f"*{clean(m.group(3))}*")
    elif m.group(4):
        for it in re.split(r'\\item',m.group(4))[1:]: out.append(f"  - In brief: {clean(it)}")
    elif m.group(5): out.append(f"  - {clean(m.group(5))}")
    elif m.group(6): out.append(f"  - {clean(m.group(6))}")
    if '\\begin{thebibliography}' in s[:m.start()]: break
print("\n".join(out))
