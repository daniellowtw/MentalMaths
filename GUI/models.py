__author__ = 'Daniel'

from PySide.QtCore import *
import operator

class MyHistoryTableModel(QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None, *args):
        """
        :param datain:lists[]
        :param headerdata:str[]
        :param parent: Defaults None
        :param args:
        :return:None
        """
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.arraydata[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headerdata[col]
        return None

    def sort(self, Ncol, order):
        """Sort table by given column number."""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))
