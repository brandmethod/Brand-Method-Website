"""Rescale the rendered deck to 1440 x 810 pt so it drops in at exactly the
same page size as the 2025/2026 edition. Vector + image content, so lossless."""
import pymupdf, sys, os
src_path = sys.argv[1]
W, H = 1440.0, 810.0
src = pymupdf.open(src_path)
out = pymupdf.open()
for i in range(src.page_count):
    pg = out.new_page(width=W, height=H)
    pg.show_pdf_page(pymupdf.Rect(0, 0, W, H), src, i)
out.set_metadata({
    "title": "ALTIGO Elevator Sdn Bhd | Company Profile 2026",
    "author": "ALTIGO Elevator Sdn Bhd",
    "subject": "Company Profile — Edition 2026, Volume 01",
    "keywords": "ALTIGO, elevator, escalator, lift, Malaysia, DOSH, EN 81-20, company profile",
    "creator": "ALTIGO Company Profile build (index.html)",
    "producer": "PyMuPDF",
})
tmp = src_path + ".tmp"
out.save(tmp, garbage=4, deflate=True, clean=True)
out.close(); src.close()
os.replace(tmp, src_path)
d = pymupdf.open(src_path)
print(f"{os.path.basename(src_path)}: {d.page_count} pages, {d[0].rect}, {os.path.getsize(src_path)//1024} KB")
