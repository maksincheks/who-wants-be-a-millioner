from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GlavWindow(object):
    def setupUi(self, GlavWindow):
        GlavWindow.setObjectName("GlavWindow")
        GlavWindow.resize(1798, 951)
        self.centralwidget = QtWidgets.QWidget(GlavWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1800, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("fon_game.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.task_A = QtWidgets.QPushButton(self.centralwidget)
        self.task_A.setGeometry(QtCore.QRect(100, 600, 750, 130))
        self.task_A.setStyleSheet("QPushButton#task_A {\n"
"    border-radius: 50px;\n"
"    background-color: rgb(0, 0, 58);\n"
"    width: 100px;\n"
"    height: 58px;\n"
"    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);\n"
"}\n"
"")
        self.task_A.setObjectName("task_A")
        self.task_B = QtWidgets.QPushButton(self.centralwidget)
        self.task_B.setGeometry(QtCore.QRect(950, 600, 750, 130))
        self.task_B.setStyleSheet("QPushButton#task_B {\n"
"    border-radius: 50px;\n"
"    background-color: rgb(0, 0, 58);\n"
"    width: 100px;\n"
"    height: 58px;\n"
"    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);\n"
"}")
        self.task_B.setObjectName("task_B")
        self.task_D = QtWidgets.QPushButton(self.centralwidget)
        self.task_D.setGeometry(QtCore.QRect(950, 760, 750, 130))
        self.task_D.setStyleSheet("QPushButton#task_D {\n"
"    border-radius: 50px;\n"
"    background-color: rgb(0, 0, 58);\n"
"    width: 100px;\n"
"    height: 58px;\n"
"    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);\n"
"}")
        self.task_D.setObjectName("task_D")
        self.task_C = QtWidgets.QPushButton(self.centralwidget)
        self.task_C.setGeometry(QtCore.QRect(100, 760, 750, 130))
        self.task_C.setStyleSheet("QPushButton#task_C {\n"
"    border-radius: 50px;\n"
"    background-color: rgb(0, 0, 58);\n"
"    width: 100px;\n"
"    height: 58px;\n"
"    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);\n"
"}")
        self.task_C.setObjectName("task_C")
        GlavWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GlavWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1798, 26))
        self.menubar.setObjectName("menubar")
        GlavWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GlavWindow)
        self.statusbar.setObjectName("statusbar")
        GlavWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GlavWindow)
        QtCore.QMetaObject.connectSlotsByName(GlavWindow)

    def retranslateUi(self, GlavWindow):
        _translate = QtCore.QCoreApplication.translate
        GlavWindow.setWindowTitle(_translate("GlavWindow", "MainWindow"))
        self.task_A.setText(_translate("GlavWindow", "сюда вводить текст"))
        self.task_B.setText(_translate("GlavWindow", "сюда вводить текст"))
        self.task_D.setText(_translate("GlavWindow", "сюда вводить текст"))
        self.task_C.setText(_translate("GlavWindow", "сюда вводить текст"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GlavWindow = QtWidgets.QMainWindow()
    ui = Ui_GlavWindow()
    ui.setupUi(GlavWindow)
    GlavWindow.show()
    sys.exit(app.exec_())
