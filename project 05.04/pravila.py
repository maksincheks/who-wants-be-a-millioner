# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rules1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RulesWindow(object):
    def setupUi(self, RulesWindow):
        RulesWindow.setObjectName("RulesWindow")
        RulesWindow.resize(661, 716)
        self.rules_widget = QtWidgets.QWidget(RulesWindow)
        self.rules_widget.setObjectName("rules_widget")
        self.label = QtWidgets.QLabel(self.rules_widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 662, 692))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/rules.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.back_rules = QtWidgets.QPushButton(self.rules_widget)
        self.back_rules.setGeometry(QtCore.QRect(5, 5, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.back_rules.setFont(font)
        self.back_rules.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: #C6C6C6;\n"
"    border: 2px solid #C6C6C6;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #B3B3B3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #A0A0A0;\n"
"}")
        self.back_rules.setObjectName("back_rules")
        RulesWindow.setCentralWidget(self.rules_widget)
        self.menubar = QtWidgets.QMenuBar(RulesWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 26))
        self.menubar.setObjectName("menubar")
        RulesWindow.setMenuBar(self.menubar)

        self.retranslateUi(RulesWindow)
        QtCore.QMetaObject.connectSlotsByName(RulesWindow)

    def retranslateUi(self, RulesWindow):
        _translate = QtCore.QCoreApplication.translate
        RulesWindow.setWindowTitle(_translate("RulesWindow", "MainWindow"))
        self.back_rules.setText(_translate("RulesWindow", "НАЗАД"))
