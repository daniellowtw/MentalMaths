# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startwidget.ui'
#
# Created: Sun Jul 19 13:27:44 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(281, 110)
        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.quickGameBtn = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quickGameBtn.sizePolicy().hasHeightForWidth())
        self.quickGameBtn.setSizePolicy(sizePolicy)
        self.quickGameBtn.setObjectName("quickGameBtn")
        self.gridLayout.addWidget(self.quickGameBtn, 0, 0, 1, 1)
        self.trainingBtn = QtGui.QPushButton(Form)
        self.trainingBtn.setObjectName("trainingBtn")
        self.gridLayout.addWidget(self.trainingBtn, 0, 1, 1, 1)
        self.settingsBtn = QtGui.QPushButton(Form)
        self.settingsBtn.setObjectName("settingsBtn")
        self.gridLayout.addWidget(self.settingsBtn, 1, 1, 1, 1)
        self.historyOrSavedBtn = QtGui.QPushButton(Form)
        self.historyOrSavedBtn.setObjectName("historyOrSavedBtn")
        self.gridLayout.addWidget(self.historyOrSavedBtn, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Mental Math", None, QtGui.QApplication.UnicodeUTF8))
        self.quickGameBtn.setText(QtGui.QApplication.translate("Form", "&Quick Game", None, QtGui.QApplication.UnicodeUTF8))
        self.trainingBtn.setText(QtGui.QApplication.translate("Form", "&Training", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsBtn.setText(QtGui.QApplication.translate("Form", "&Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.historyOrSavedBtn.setText(QtGui.QApplication.translate("Form", "H&istory/Saved Questions", None, QtGui.QApplication.UnicodeUTF8))

