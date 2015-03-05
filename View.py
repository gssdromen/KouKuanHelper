# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View.ui'
#
# Created: Thu Mar 05 12:52:18 2015
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(807, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_status1 = QtGui.QLabel(self.centralwidget)
        self.label_status1.setGeometry(QtCore.QRect(30, 10, 181, 31))
        self.label_status1.setObjectName(_fromUtf8("label_status1"))
        self.label_status2 = QtGui.QLabel(self.centralwidget)
        self.label_status2.setGeometry(QtCore.QRect(30, 50, 181, 31))
        self.label_status2.setObjectName(_fromUtf8("label_status2"))
        self.text_time = QtGui.QTextEdit(self.centralwidget)
        self.text_time.setGeometry(QtCore.QRect(30, 100, 181, 101))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.text_time.setFont(font)
        self.text_time.setReadOnly(True)
        self.text_time.setObjectName(_fromUtf8("text_time"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_status1.setText(_translate("MainWindow", "TextLabel", None))
        self.label_status2.setText(_translate("MainWindow", "TextLabel", None))

