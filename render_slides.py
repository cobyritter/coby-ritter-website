import os
import subprocess
import sys

try:
    import fitz
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf"])
    import fitz

pdfs = [
    r"C:\Users\cobyr\personal-website\assets\slides\Ritter.Coby.PITCHDECK (Summary Only).pdf",
    r"C:\Users\cobyr\personal-website\assets\slides\GE Vernova Pitch Slides (Summary Only).pdf",
]

out_dir = r"C:\Users\cobyr\personal-website\assets\slides"
os.makedirs(out_dir, exist_ok=True)

for pdf in pdfs:
    if not os.path.exists(pdf):
        print(f"MISSING: {pdf}")
        continue

    doc = fitz.open(pdf)
    base = os.path.splitext(os.path.basename(pdf))[0]
    print(f"EXPORTING: {pdf}")

    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        out = os.path.join(out_dir, f"{base}-page-{page_num + 1}.png")
        pix.save(out)
        print(f"SAVED: {out}")

    doc.close()

print("DONE")
