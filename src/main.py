import sys

from PySide6 import QtWidgets as qw

from src.events import init_gui_events
from src.gui.gui import Ui_Pdf2Cbz
from src.search import search_pdf_file
from src.table import add_items_to_table


class Pdf2Cbz(Ui_Pdf2Cbz, qw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        init_gui_events(self)

    def add_pdf_files(self):
        files = search_pdf_file()
        if not files:
            return
        add_items_to_table(self, files)


def run():
    app = qw.QApplication(sys.argv)
    gui = Pdf2Cbz()
    gui.show()
    sys.exit(app.exec_())
