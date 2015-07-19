# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gamewidget.ui'
#
# Created: Sun Jul 19 13:27:41 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_gameWidget(object):
    def setupUi(self, gameWidget):
        gameWidget.setObjectName("gameWidget")
        gameWidget.resize(400, 300)
        self.widget = QtGui.QWidget(gameWidget)
        self.widget.setGeometry(QtCore.QRect(100, 80, 135, 41))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.questionLabel = QtGui.QLabel(self.widget)
        self.questionLabel.setObjectName("questionLabel")
        self.verticalLayout.addWidget(self.questionLabel)
        self.userInputLineEdit = QtGui.QLineEdit(self.widget)
        self.userInputLineEdit.setObjectName("userInputLineEdit")
        self.verticalLayout.addWidget(self.userInputLineEdit)

        self.retranslateUi(gameWidget)
        QtCore.QMetaObject.connectSlotsByName(gameWidget)

    def retranslateUi(self, gameWidget):
        gameWidget.setWindowTitle(QtGui.QApplication.translate("gameWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.questionLabel.setText(QtGui.QApplication.translate("gameWidget", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

