import os
import sys

try:
    import fitz
except Exception:
    print('PyMuPDF not installed. Installing...')
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pymupdf'])
    import fitz

pdfs = [
    r'C:\Users\cobyr\Downloads\Ritter.Coby.PITCHDECK (Final Recommendation only).pdf',
    r'C:\Users\cobyr\OneDrive\Documents\Valuation - GEVernova - Copy.pdf',
]

out_dir = r'C:\Users\cobyr\personal-website\assets\slides'
os.makedirs(out_dir, exist_ok=True)

for pdf in pdfs:
    if not os.path.exists(pdf):
        print(f'MISSING: {pdf}')
        continue

    doc = fitz.open(pdf)
    base = os.path.splitext(os.path.basename(pdf))[0]
    print(f'EXPORTING: {pdf}')

    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
        out = os.path.join(out_dir, f'{base}-page-{page_num + 1}.png')
        pix.save(out)
        print(f'SAVED: {out}')

    doc.close()

print('DONE')
