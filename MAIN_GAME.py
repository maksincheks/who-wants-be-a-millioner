import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl


    #КЛАСС ВТОРОГО ОКНА


class Take_level(QMainWindow):
    def __init__(self):
        super(Take_level, self).__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setStyleSheet("background-color: rgb(168, 215, 171);")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)


        self.level_widget = QtWidgets.QWidget(self)
        self.level_widget.setObjectName("level_widget")

        self.menu_widget = None


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
        self.back_second.clicked.connect(self.back_to_menu)

    def back_to_menu(self):
        self.close()  # Закрываем текущее окно
        if not self.menu_widget:
            self.menu_widget = MainWindow()
        self.menu_widget.show()
        #КЛАСС ПРАВИЛ

class RulesWindow(QMainWindow):
    def __init__(self):
        super(RulesWindow, self).__init__()
        self.setGeometry(650, 200, 661, 692)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.rules_widget = QtWidgets.QWidget(self)
        self.rules_widget.setObjectName("rules_widget")

        self.label = QtWidgets.QLabel(self.rules_widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 662, 692))
        self.label.setPixmap(QtGui.QPixmap("image/rules.png"))

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
        self.back_rules.setText("НАЗАД")
        self.setCentralWidget(self.rules_widget)




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setStyleSheet("background-color: rgb(240, 245, 253);")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.showFullScreen()

        self.menu_widget = QtWidgets.QWidget(self)
        self.menu_widget.setObjectName("menu_widget")

        self.level_widget = Take_level()

        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("image/song1.mp3")))

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
        self.start_game.clicked.connect(self.switch_widget)


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
        self.rules_game.clicked.connect(self.openRules)


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
        self.pushButton.clicked.connect(self.togglePlayState)
        self.fon_menu = QtWidgets.QLabel(self.menu_widget)
        self.fon_menu.setGeometry(QtCore.QRect(670, 120, 1031, 871))
        self.fon_menu.setPixmap(QtGui.QPixmap("image/menushka.png"))
        self.fon_menu.setObjectName("fon_menu")
        self.setCentralWidget(self.menu_widget)
        self.rules_window = None

    def openRules(self):
        def returnToMain():
            if self.rules_window:
                self.rules_window.close()
                self.rules_window = None

        if not self.rules_window:
            self.rules_window = RulesWindow()
            self.rules_window.show()
            self.rules_window.back_rules.clicked.connect(returnToMain)


    def switch_widget(self):
        if self.centralWidget() == self.menu_widget:
            self.setCentralWidget(self.level_widget)
        else:
            self.setCentralWidget(self.menu_widget)
    def togglePlayState(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

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