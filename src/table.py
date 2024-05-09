from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.main import Pdf2Cbz

from PySide6 import QtWidgets as qw


def add_items_to_table(self: "Pdf2Cbz", item_list: list[str]):
    row_count = self.table_conversion.rowCount()
    self.table_conversion.setRowCount(row_count + len(item_list))
    for i, item in enumerate(item_list):
        widget_item = qw.QTableWidgetItem(item)
        self.table_conversion.setItem(row_count+i, 0, widget_item)
