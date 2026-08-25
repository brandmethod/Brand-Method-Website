import subprocess, re, base64, urllib.parse, os, json
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/120.0.0.0 Safari/537.36")
def get(url, binary=False):
    r = subprocess.run(["curl","-sSL","--max-time","60","-A",UA,url],
                       capture_output=True)
    if r.returncode: raise RuntimeError(url+" -> "+r.stderr.decode()[:200])
    return r.stdout if binary else r.stdout.decode()

REQ = [
  ("Archivo",        "family=Archivo:wdth,wght@62..125,400..900", None),
  ("Figtree",        "family=Figtree:wght@300..900",              None),
  ("JetBrains Mono", "family=JetBrains+Mono:wght@400..700",       None),
  ("Noto Sans SC",   "family=Noto+Sans+SC:wght@400..700",         "唯一清真方便面中文"),
  ("Noto Naskh Arabic","family=Noto+Naskh+Arabic:wght@400..700",  "نودلزسريعةالتحضيرحلالالعربية "),
]
KEEP = ("latin", "latin-ext")
faces, total = [], 0
for name, fam, text in REQ:
    url = "https://fonts.googleapis.com/css2?" + fam + "&display=swap"
    if text: url += "&text=" + urllib.parse.quote(text)
    css = get(url)
    blocks = re.findall(r"/\*\s*([\w\-\[\]]+)\s*\*/\s*(@font-face\s*\{.*?\})", css, re.S)
    if not blocks:  # text-subset responses carry no subset comments
        blocks = [("subset", b) for b in re.findall(r"@font-face\s*\{.*?\}", css, re.S)]
    picked = 0
    for subset, block in blocks:
        if not text and subset not in KEEP: continue
        m = re.search(r"url\((https://[^)]+)\)\s*format\(\x27woff2\x27\)", block)
        if not m: continue
        data = get(m.group(1), binary=True); total += len(data)
        b64 = base64.b64encode(data).decode()
        faces.append(re.sub(r"url\(https://[^)]+\)\s*format\('woff2'\)",
                            f"url(data:font/woff2;base64,{b64}) format('woff2')", block))
        picked += 1
    print(f"  {name:18s} {picked} face(s)")
out = "\n".join(faces)
open("fonts/embedded.css","w",encoding="utf-8").write(out)
print(f"raw woff2 {total/1024:.0f} KB  ->  css {len(out)/1024:.0f} KB")
