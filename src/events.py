from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.main import Pdf2Cbz


def init_gui_events(self: "Pdf2Cbz"):
    self.pb_add_file.clicked.connect(self.add_pdf_files)
