from PyQt5 import QtCore, QtGui, QtWidgets
from glav_menu import Ui_GlavWindow


class Ui_sec_window(object):
    def setupUi(self, sec_window):
        sec_window.setObjectName("sec_window")
        sec_window.resize(1800, 989)
        self.centralwidget = QtWidgets.QWidget(sec_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1800, 950))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("03RESED (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.school_but = QtWidgets.QPushButton(self.centralwidget)
        self.school_but.setGeometry(QtCore.QRect(1350, 350, 360, 140))
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
        self.student_but = QtWidgets.QPushButton(self.centralwidget)
        self.student_but.setGeometry(QtCore.QRect(1350, 500, 360, 140))
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
        self.genius_but = QtWidgets.QPushButton(self.centralwidget)
        self.genius_but.setGeometry(QtCore.QRect(1350, 650, 360, 140))
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
        self.back_second = QtWidgets.QPushButton(self.centralwidget)
        self.back_second.setGeometry(QtCore.QRect(2, 1, 141, 51))
        self.back_second.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-left: 5px; /* сдвигаем изображение влево при нажатии */\n"
"    padding-top: 5px; /* сдвигаем изображение вверх при нажатии */\n"
"}")
        self.back_second.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("back_rules.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_second.setIcon(icon)
        self.back_second.setIconSize(QtCore.QSize(200, 200))
        self.back_second.setFlat(True)
        self.back_second.setObjectName("back_second")
        sec_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(sec_window)
        self.statusbar.setObjectName("statusbar")
        sec_window.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(sec_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1800, 26))
        self.menubar.setObjectName("menubar")
        sec_window.setMenuBar(self.menubar)
        self.school_but.clicked.connect(self.openGlWindow)

        self.retranslateUi(sec_window)
        QtCore.QMetaObject.connectSlotsByName(sec_window)

    def openGlWindow(self):
        global GlavWindow
        GlavWindow = QtWidgets.QMainWindow()
        ui = Ui_GlavWindow()
        ui.setupUi(GlavWindow)
        GlavWindow.show()
        sec_window.hide()


    def retranslateUi(self, sec_window):
        _translate = QtCore.QCoreApplication.translate
        sec_window.setWindowTitle(_translate("sec_window", "MainWindow"))
        self.school_but.setText(_translate("sec_window", "ШКОЛЬНИК"))
        self.student_but.setText(_translate("sec_window", "СТУДЕНТ"))
        self.genius_but.setText(_translate("sec_window", "ГЕНИЙ"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sec_window = QtWidgets.QMainWindow()
    ui = Ui_sec_window()
    ui.setupUi(sec_window)
    sec_window.show()
    sys.exit(app.exec_())
