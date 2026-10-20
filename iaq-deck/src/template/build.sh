#!/bin/sh
# the whole handover in one pass: pages, template, the two merged, the layouts
# wired into the master, the template pages hidden from the slideshow, fonts in
set -e
D=/home/user/Brand-Method-Website/iaq-deck
cd "$D/src"
python3 build_template.py            # the empty layouts
python3 build_template.py paired     # the same, each beside a worked example
cd "$D/src/template"
python3 build_combined.py            # deck pages + template pages, one file
cd "$1"                              # the pipeline's working directory
python3 extract.py
python3 rasterize.py
python3 emit.py
python3 hide.py IAQ-Deck-With-Template.pptx 68
python3 combine.py IAQ-Deck-With-Template.pptx IAQ-Company-Deck-2026.pptx
python3 embed.py IAQ-Company-Deck-2026.pptx
