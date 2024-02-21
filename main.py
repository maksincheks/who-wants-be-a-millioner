import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog
from ConfigFW import Ui_MainWindow
from ConfigSW import Ui_sec_window
from ConfigRW import Ui_Dialog
from glav_menu import Ui_GlavWindow

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def close_application():
    reply = QMessageBox()
    reply.setWindowTitle('Выход')
    reply.setText("Вы уверены, что хотите покинуть приложение?")
    reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    reply.button(QMessageBox.Yes).setText('Да')
    reply.button(QMessageBox.No).setText('Нет')

    if reply.exec_() == QMessageBox.Yes:
        sys.exit()


ui.exit_game.clicked.connect(close_application)

def openSecWin():
    global sec_window
    sec_window = QtWidgets.QMainWindow()
    ui = Ui_sec_window()
    ui.setupUi(sec_window)
    MainWindow.hide()
    sec_window.show()

    def returnToMain():
        sec_window.close()
        MainWindow.show()
    ui.back_second.clicked.connect(returnToMain)

ui.start_game.clicked.connect(openSecWin)

def openRules():
    global Dialog
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    def returnToMain():
        Dialog.close()
    ui.pushButton.clicked.connect(returnToMain)

ui.rules_game.clicked.connect(openRules)

sys.exit(app.exec_())