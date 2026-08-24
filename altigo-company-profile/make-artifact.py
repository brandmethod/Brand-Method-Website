"""Build a single self-contained viewer page from index.html.

Inlines every asset as a data URI, strips the print/standalone chrome from the
deck stylesheet, and wraps each 1440x810 slide in a scaled viewer shell.
Output is body-level HTML for publishing as an Artifact.
"""
import base64, mimetypes, os, re, sys

R = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(R, "index.html"), encoding="utf-8").read()

def data_uri(rel):
    path = os.path.join(R, rel)
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()

# ---- pull the three parts we need out of the standalone document ----
style = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
body  = re.search(r"<body>(.*?)</body>", src, re.S).group(1)

# ---- deck stylesheet: drop everything that assumes it owns the document ----
style = re.sub(r"@font-face\{\s*font-family:'Jakarta';.*?\}", "", style, flags=re.S)
style = re.sub(r"\nbody\{[^}]*\}", "", style, count=1)
style = re.sub(r"/\* screen-only page framing \*/\s*@media screen\{.*?\n\}\n", "", style, flags=re.S)
style = re.sub(r"/\* =+ PRINT =+ \*/\s*@page\{[^}]*\}\s*@media print\{.*?\n\}\n", "", style, flags=re.S)
# the deck's own font stack, now served by the inlined face below
style = style.replace("--font:'Axiforma','Jakarta','Plus Jakarta Sans',system-ui",
                      "--font:'Axiforma','ALTIGO Sans','Plus Jakarta Sans',system-ui")

# ---- inline the variable font and every image ----
font = data_uri("fonts/PlusJakartaSans-latin-var.woff2")
face = ("@font-face{font-family:'ALTIGO Sans';src:url(%s) format('woff2-variations');"
        "font-weight:200 800;font-style:normal;font-display:block}\n" % font)

seen = {}
def sub_img(m):
    rel = m.group(1)
    if rel not in seen:
        seen[rel] = data_uri(rel)
    return 'src="%s"' % seen[rel]
body = re.sub(r'src="(assets/[^"]+)"', sub_img, body)

logo_colour = seen["assets/logo-wordmark-colour.png"]
logo_white  = seen["assets/logo-wordmark-white.png"]

# ---- wrap each slide in the viewer shell ----
slides = re.findall(r"(<section class=\"page[^\"]*\">.*?</section>)", body, re.S)
assert len(slides) == 41, f"expected 41 slides, found {len(slides)}"

sprite = re.search(r'(<svg id="sprite".*?</svg>)', body, re.S).group(1)

TITLES = [
 "Cover","Positioning Statement","Table of Contents","Company at a Glance",
 "Chapter 00 — Company Overview","Our Objective","Our Aim","Vision & Mission",
 "Operating Footprint","Chapter 01 — Brand Identity","Brand USP","The ALTIGO Difference",
 "Our Values","People Behind the Brand","Company Culture","Organisation Chart",
 "Chapter 02 — Market & Performance","Market Statistics","Target Market",
 "Chapter 03 — Products & Services","Our Products","Vertical Transport for People",
 "Movement at Volume","Service Scope","Maintenance Programme","Product Journey",
 "Chapter 04 — Client Testimonials","What Our Clients Say","Chapter 05 — Our Activities",
 "Our Activities","Chapter 06 — Achievements & Certifications","Our Track Record",
 "Our Achievements","Safety & Compliance","EU Type Examination","Certified Performance Range",
 "Chapter 07 — Project References & Contact","Latest Project References",
 "Company Info & History","Contact Information","Back Cover",
]
assert len(TITLES) == 41

shell = []
for i, s in enumerate(slides):
    n = i + 1
    shell.append(
        f'<section class="v-slide" id="p{n}" aria-label="Page {n}: {TITLES[i]}">\n'
        f'  <div class="v-slide-bar"><span class="v-folio">{n:02d}</span>'
        f'<span class="v-slide-name">{TITLES[i]}</span></div>\n'
        f'  <div class="v-stage"><div class="v-fit">{s}</div></div>\n'
        f'</section>'
    )

open(os.path.join(R, "artifact-body.html"), "w", encoding="utf-8").write("")
print("slides:", len(slides))
print("font b64 KB:", len(font)//1024)
print("unique images:", len(seen), "| inlined KB:", sum(len(v) for v in seen.values())//1024)

# stash the pieces for the assembler
import json
json.dump({"style": style, "face": face, "sprite": sprite,
           "shell": "\n\n".join(shell),
           "logo_colour": logo_colour, "logo_white": logo_white},
          open(os.path.join(R, ".artifact-parts.json"), "w"))
