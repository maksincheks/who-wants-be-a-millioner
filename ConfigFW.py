from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1799, 1003)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1800, 950))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("1626802791_6-kartinkin-com-p-bel.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.start_game = QtWidgets.QPushButton(self.centralwidget)
        self.start_game.setGeometry(QtCore.QRect(100, 300, 361, 141))
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
        self.start_game.setObjectName("start_game")
        self.rules_game = QtWidgets.QPushButton(self.centralwidget)
        self.rules_game.setGeometry(QtCore.QRect(100, 500, 361, 141))
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
        self.rules_game.setObjectName("rules_game")
        self.exit_game = QtWidgets.QPushButton(self.centralwidget)
        self.exit_game.setGeometry(QtCore.QRect(100, 700, 361, 141))
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
        self.exit_game.setObjectName("exit_game")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1799, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_game.setText(_translate("MainWindow", "НАЧАТЬ ИГРУ"))
        self.rules_game.setText(_translate("MainWindow", "ОБ ИГРЕ"))
        self.exit_game.setText(_translate("MainWindow", "ВЫХОД"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


