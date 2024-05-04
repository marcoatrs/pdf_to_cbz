import shutil
import zipfile
from pathlib import Path

import fitz


def pdf_to_cbz(pdf_path: str | Path, cbz_output_path: str | Path = "output.cbz", image_ext: str = "jpg"):
    if isinstance(pdf_path, str):
        pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        raise FileNotFoundError(f"pdf {pdf_path.name} not found")

    temp_folder = Path(__file__).parent / ".temp"
    temp_folder.mkdir(exist_ok=True)

    with fitz.open(pdf_path) as document:
        cbz = zipfile.ZipFile(cbz_output_path, mode="w", compression=zipfile.ZIP_DEFLATED)
        for i, page in enumerate(document):
            image_path = temp_folder / f"image_{i}.{image_ext}"
            page.get_pixmap().save(image_path)
            cbz.write(str(image_path), image_path.name)

    shutil.rmtree(str(temp_folder))

    print("Done!")
