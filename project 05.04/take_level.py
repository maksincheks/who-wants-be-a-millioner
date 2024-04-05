# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Take_level(QMainWindow):
    def __init__(self):
        super(Take_level, self).__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setStyleSheet("background-color: rgb(168, 215, 171);")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)


        self.level_widget = QtWidgets.QWidget(self)
        self.level_widget.setObjectName("level_widget")


        self.school_but = QtWidgets.QPushButton(self.level_widget)
        self.school_but.setGeometry(QtCore.QRect(1450, 550, 360, 140))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.school_but.setFont(font)
        self.school_but.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(238, 238, 238); /* тёмно-белый цвет при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white; /* белый цвет при нажатии */\n"
"}\n"
"")
        self.school_but.setObjectName("school_but")
        self.school_but.setText('ШКОЛЬНИК')
        self.student_but = QtWidgets.QPushButton(self.level_widget)
        self.student_but.setGeometry(QtCore.QRect(1450, 700, 360, 140))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.student_but.setFont(font)
        self.student_but.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(238, 238, 238); /* тёмно-белый цвет при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white; /* белый цвет при нажатии */\n"
"}\n"
"")
        self.student_but.setObjectName("student_but")
        self.student_but.setText('СТУДЕНТ')
        self.genius_but = QtWidgets.QPushButton(self.level_widget)
        self.genius_but.setGeometry(QtCore.QRect(1450, 850, 360, 140))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.genius_but.setFont(font)
        self.genius_but.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(238, 238, 238); /* тёмно-белый цвет при наведении */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: white; /* белый цвет при нажатии */\n"
"}\n"
"")
        self.genius_but.setObjectName("genius_but")
        self.genius_but.setText('ГЕНИЙ')
        self.label = QtWidgets.QLabel(self.level_widget)
        self.label.setGeometry(QtCore.QRect(20, 65, 1000, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/snapedit_1709108545286.png.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.back_second = QtWidgets.QPushButton(self.level_widget)
        self.back_second.setGeometry(QtCore.QRect(2, -3, 161, 61))
        self.back_second.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px; /* сдвигаем изображение влево при нажатии */\n"
"    padding-top: 5px; /* сдвигаем изображение вверх при нажатии */\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/back_rules.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_second.setIcon(icon)
        self.back_second.setIconSize(QtCore.QSize(150, 100))
        self.back_second.setObjectName("back_second")
        self.setCentralWidget(self.level_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Take_level()

    window.show()
    sys.exit(app.exec())