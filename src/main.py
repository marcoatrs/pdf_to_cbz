import sys

from PySide6 import QtWidgets as qw

from src.gui.gui import Ui_Pdf2Cbz


class Pdf2Cbz(Ui_Pdf2Cbz, qw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def run():
    app = qw.QApplication(sys.argv)
    gui = Pdf2Cbz()
    gui.show()
    sys.exit(app.exec_())
