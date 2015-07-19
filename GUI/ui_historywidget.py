# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historywidget.ui'
#
# Created: Sun Jul 19 13:27:42 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.TabWidget = QtGui.QTabWidget(Dialog)
        self.TabWidget.setObjectName("TabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.historyTableView = QtGui.QTableView(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.historyTableView.sizePolicy().hasHeightForWidth())
        self.historyTableView.setSizePolicy(sizePolicy)
        self.historyTableView.setObjectName("historyTableView")
        self.horizontalLayout_2.addWidget(self.historyTableView)
        self.TabWidget.addTab(self.tab, "")
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName("tab1")
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.savedListWidget = QtGui.QListWidget(self.tab1)
        self.savedListWidget.setObjectName("savedListWidget")
        self.horizontalLayout.addWidget(self.savedListWidget)
        self.TabWidget.addTab(self.tab1, "")
        self.horizontalLayout_3.addWidget(self.TabWidget)

        self.retranslateUi(Dialog)
        self.TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.TabWidget.setWindowTitle(QtGui.QApplication.translate("Dialog", "TabWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "&History", None, QtGui.QApplication.UnicodeUTF8))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab1), QtGui.QApplication.translate("Dialog", "&Saved", None, QtGui.QApplication.UnicodeUTF8))

