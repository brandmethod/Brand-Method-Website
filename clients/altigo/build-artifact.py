#!/usr/bin/env python3
"""Convert the standalone profile into Artifact page-content form.

The Artifact host supplies <!doctype>, <html>, <head> and <body>, so this
strips our own document scaffolding and hoists <title> to the very top —
the host only scans the first 8KB for it, and the inlined woff2 faces are
far larger than that.  Nothing else about the deck is altered.
"""
import re,sys,pathlib
SRC=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else 'ALTIGO_Company_Profile_2026.html')
DST=pathlib.Path(sys.argv[2] if len(sys.argv)>2 else 'altigo-profile.artifact.html')
s=SRC.read_text(encoding='utf-8')
head=s[s.index('<head>')+6:s.index('</head>')]
body=s[s.index('<body>')+6:s.rindex('</body>')]
keep=''.join(m.group(0) for m in re.finditer(r'<style>.*?</style>|<script>.*?</script>',head,re.S))
assert '<style>' in keep and '@font-face' in keep, 'stylesheet not carried over'
out='<title>ALTIGO Company Profile 2026</title>\n'+keep+'\n'+body.strip()+'\n'
for bad in ('<!DOCTYPE','<html','</html>','<head>','</head>','<body>','</body>'):
    assert bad not in out, f'document scaffolding survived: {bad}'
DST.write_text(out,encoding='utf-8')
print(f"{DST}  {len(out)//1024} KB  (source {len(s)//1024} KB)")
print("title index:",out.index('<title>'),"· slides:",out.count('<section class="slide'))
