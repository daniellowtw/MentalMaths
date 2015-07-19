# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created: Sun Jul 19 13:27:43 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(Menu)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.myListView = QtGui.QListView(Menu)
        self.myListView.setObjectName("myListView")
        self.horizontalLayout.addWidget(self.myListView)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QtGui.QApplication.translate("Menu", "Form", None, QtGui.QApplication.UnicodeUTF8))

