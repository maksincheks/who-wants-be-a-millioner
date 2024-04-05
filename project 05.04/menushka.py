# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setStyleSheet("background-color: rgb(240, 245, 253);")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.menu_widget = QtWidgets.QWidget(self)
        self.menu_widget.setObjectName("menu_widget")

        self.start_game = QtWidgets.QPushButton(self.menu_widget)
        self.start_game.setGeometry(QtCore.QRect(100, 400, 361, 141))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.start_game.setFont(font)
        self.start_game.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A9A9A9; /* тёмно-серый цвет при наведении */\n"
"}")
        self.start_game.setText('НАЧАТЬ ИГРУ')


        self.rules_game = QtWidgets.QPushButton(self.menu_widget)
        self.rules_game.setGeometry(QtCore.QRect(100, 600, 361, 141))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.rules_game.setFont(font)
        self.rules_game.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A9A9A9; /* тёмно-серый цвет при наведении */\n"
"}")
        self.rules_game.setText('ОБ ИГРЕ')


        self.exit_game = QtWidgets.QPushButton(self.menu_widget)
        self.exit_game.setGeometry(QtCore.QRect(100, 800, 361, 141))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.exit_game.setFont(font)
        self.exit_game.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #A9A9A9; /* тёмно-серый цвет при наведении */\n"
"}")
        self.exit_game.setText('ВЫХОД')
        self.exit_game.clicked.connect(self.close_application)


        self.pushButton = QtWidgets.QPushButton(self.menu_widget)
        self.pushButton.setGeometry(QtCore.QRect(1800, 960, 91, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/unmute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(120, 70))
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")

        self.fon_menu = QtWidgets.QLabel(self.menu_widget)
        self.fon_menu.setGeometry(QtCore.QRect(670, 120, 1031, 871))
        self.fon_menu.setPixmap(QtGui.QPixmap("image/menushka.png"))
        self.fon_menu.setObjectName("fon_menu")
        self.setCentralWidget(self.menu_widget)

    def close_application(self):
        reply = QMessageBox()
        reply.setWindowTitle('Выход')
        reply.setText("Вы уверены, что хотите покинуть приложение?")
        reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        reply.button(QMessageBox.Yes).setText('Да')
        reply.button(QMessageBox.No).setText('Нет')

        if reply.exec_() == QMessageBox.Yes:
            sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())