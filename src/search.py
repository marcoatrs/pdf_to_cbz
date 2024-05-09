import sys
from pathlib import Path

from PySide6 import QtWidgets as qw


if getattr(sys, "frozen", False):
    _SRC_PATH = Path(sys.executable).parent
else:
    _SRC_PATH = Path(__file__).parents[1]


def search_pdf_file() -> list:
    file_dialog = qw.QFileDialog()
    pdf_list, _ = file_dialog.getOpenFileNames(
        caption="Select one or more pdf files to open",
        dir=str(_SRC_PATH),
        filter="PDF Files (*.pdf)",
    )
    return pdf_list
