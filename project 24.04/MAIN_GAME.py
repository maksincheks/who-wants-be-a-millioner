import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QTimer
from random import shuffle, sample, choice
import random


class GameWindow(QMainWindow):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.showFullScreen()

        self.total_money = 1000

        self.game_widget = QtWidgets.QWidget(self)
        self.game_widget.setObjectName("game_widget")

        self.media_player = QMediaPlayer()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile("sounds/song1.mp3")))
        self.media_player.setVolume(10)


        self.button_click_sound_set = QSoundEffect()
        self.button_click_sound_set.setSource(QUrl.fromLocalFile("sounds/button.wav"))
        self.button_click_sound_set.setVolume(0.3)

        self.button_click_sound_5050 = QSoundEffect()
        self.button_click_sound_5050.setSource(QUrl.fromLocalFile("sounds/hint_5050.wav"))
        self.button_click_sound_5050.setVolume(0.3)

        self.button_click_sound_call = QSoundEffect()
        self.button_click_sound_call.setSource(QUrl.fromLocalFile("sounds/call_friends.wav"))
        self.button_click_sound_call.setVolume(0.2)

        self.fon_main = QtWidgets.QLabel(self.game_widget)
        self.fon_main.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.fon_main.setPixmap(QtGui.QPixmap("image/fon_game.jpg"))
        self.fon_main.setObjectName('label')

        self.money_label = QtWidgets.QLabel(self.game_widget)
        self.money_label.setGeometry(1650,130, 300, 100)
        self.money_label.setText('Выигрыш: $0')
        self.money_label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: black")
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(65)
        self.money_label.setFont(font)

        self.task_A = QtWidgets.QPushButton(self.game_widget)
        self.task_A.setGeometry(QtCore.QRect(100, 680, 820, 130))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(65)
        self.task_A.setFont(font)
        self.task_A.setStyleSheet("QPushButton#task_A {\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "    border-radius: 50px;\n"
                                  "    background-color: rgb(0, 0, 58);\n"
                                  "    width: 100px;\n"
                                  "    height: 58px;\n"
                                  "    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);\n"
                                  "}\n"
                                  "QPushButton#task_A:pressed {\n"
                                  "    background-color: rgb(255, 165, 0); /* Изменяем цвет при нажатии на оранжевый */\n"
                                  "}")
        self.task_A.setObjectName("task_A")
        self.task_A.setText('Текст ответа А')


        self.task_B = QtWidgets.QPushButton(self.game_widget)
        self.task_B.setGeometry(QtCore.QRect(1000, 680, 820, 130))
        self.task_B.setFont(font)
        self.task_B.setStyleSheet("QPushButton#task_B {\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "    border-radius: 50px;\n"
                                  "    background-color: rgb(0, 0, 58);\n"
                                  "    width: 100px;\n"
                                  "    height: 58px;\n"
                                  "    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);\n"
                                  "}\n"
                                  "QPushButton#task_B:pressed {\n"
                                  "    background-color: rgb(255, 165, 0); /* Изменяем цвет при нажатии на оранжевый */\n"
                                  "}")
        self.task_B.setObjectName("task_B")
        self.task_B.setText('Текст ответа В')
        self.task_D = QtWidgets.QPushButton(self.game_widget)
        self.task_D.setGeometry(QtCore.QRect(1000, 830, 820, 130))
        self.task_D.setFont(font)
        self.task_D.setStyleSheet("QPushButton#task_D {\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "    border-radius: 50px;\n"
                                  "    background-color: rgb(0, 0, 58);\n"
                                  "    width: 100px;\n"
                                  "    height: 58px;\n"
                                  "    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);\n"
                                  "}\n"
                                  "QPushButton#task_D:pressed {\n"
                                  "    background-color: rgb(255, 165, 0); /* Изменяем цвет при нажатии на оранжевый */\n"
                                  "}")
        self.task_D.setObjectName("task_D")
        self.task_D.setText('Текст ответа D')
        self.task_C = QtWidgets.QPushButton(self.game_widget)
        self.task_C.setGeometry(QtCore.QRect(100, 830, 820, 130))
        self.task_C.setFont(font)
        self.task_C.setStyleSheet("QPushButton#task_C {\n"
                                  "    color: rgb(255, 255, 255);\n"
                                  "    border-radius: 50px;\n"
                                  "    background-color: rgb(0, 0, 58);\n"
                                  "    width: 100px;\n"
                                  "    height: 58px;\n"
                                  "    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);\n"
                                  "}\n"
                                  "QPushButton#task_C:pressed {\n"
                                  "    background-color: rgb(255, 165, 0);\n"
                                  "}")
        self.task_C.setObjectName("task_C")
        self.task_C.setText('Текст ответа С')
        self.settings_but = QtWidgets.QPushButton(self.game_widget)
        self.settings_but.setGeometry(QtCore.QRect(10, 10, 81, 81))
        self.settings_but.setStyleSheet("QPushButton {\n"
"    border-radius: 40px;\n"
"    padding: 5px;\n"
"    background-color: black;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #c8c8c8;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_but.setIcon(icon)
        self.settings_but.setIconSize(QtCore.QSize(200, 85))
        self.settings_but.setObjectName("settings_but")
        self.settings_but.clicked.connect(self.open_set)
        self.hint_1 = QtWidgets.QPushButton(self.game_widget)
        self.hint_1.setGeometry(QtCore.QRect(1300, 20, 180, 80))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.hint_1.setFont(font)
        self.hint_1.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px; \n"
"    background-color: rgb(170, 0, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #f39c12; /* Цвет кнопки при нажатии */\n"
"}")
        self.hint_1.setIconSize(QtCore.QSize(150, 150))
        self.hint_1.setObjectName("hint_1")
        self.hint_1.setText('50/50')
        self.hint_1.clicked.connect(self.clicked_hint1)
        self.hint_2 = QtWidgets.QPushButton(self.game_widget)
        self.hint_2.setGeometry(QtCore.QRect(1500, 20, 180, 80))
        self.hint_2.setFont(font)
        self.hint_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px; \n"
"    background-color: rgb(170, 0, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #f39c12; /* Цвет кнопки при нажатии */\n"
"}")
        self.hint_2.setIconSize(QtCore.QSize(150, 150))
        self.hint_2.setObjectName("hint_2")
        self.hint_2.setText('УДАЧ-\nЛИВЫЙ')
        self.hint_2.clicked.connect(self.clicked_hint2)
        self.hint_3 = QtWidgets.QPushButton(self.game_widget)
        self.hint_3.setGeometry(QtCore.QRect(1700, 20, 180, 80))
        self.hint_3.setFont(font)
        self.hint_3.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    border-radius: 20px; \n"
"    background-color: rgb(170, 0, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #f39c12; /* Цвет кнопки при нажатии */\n"
"}")
        self.hint_3.setIconSize(QtCore.QSize(150, 150))
        self.hint_3.setObjectName("hint_3")
        self.hint_3.setText('ЗАМЕНА\nВОПРОСА')
        self.hint_3.clicked.connect(self.clicked_hint3)

        self.vvod_task = QtWidgets.QLabel(self.game_widget)
        self.vvod_task.setGeometry(QtCore.QRect(550, 150, 800, 230))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vvod_task.setFont(font)
        self.vvod_task.setAlignment(QtCore.Qt.AlignCenter)
        self.vvod_task.setStyleSheet("    border-radius: 40px;\n"
"    background-color: rgb(0, 0, 58);\n"
"    color: rgb(255, 255, 255);")
        self.vvod_task.setObjectName("vvod_task")
        self.setCentralWidget(self.game_widget)

        self.win_text = QLabel(self)
        self.win_text.setGeometry(650, 400, 600,50)
        self.win_text.setObjectName('win_text')
        self.win_text.setText('Поздравляем! Вы выиграли 1 000 000')
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(100)
        self.win_text.hide()
        self.win_text.setStyleSheet("    color: green;\n"
                                    "background-color: rgba(255, 255, 255, 0);")
        self.win_text.setFont(font)


        self.label_set = QtWidgets.QLabel(self.game_widget)
        self.label_set.setGeometry(QtCore.QRect(604, 342, 707, 326))
        self.label_set.setPixmap(QtGui.QPixmap("image/settings (2).png"))
        self.label_set.setObjectName("label")
        self.label_set.hide()
        self.label_set.setStyleSheet("border: 5px solid orange;")

        self.cont_game = QtWidgets.QPushButton(self.game_widget)
        self.cont_game.setGeometry(QtCore.QRect(800, 400, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.cont_game.setFont(font)
        self.cont_game.setStyleSheet("color: rgb(255, 255, 255);")
        self.cont_game.setObjectName("cont_game")
        self.cont_game.setFlat(True)
        self.cont_game.setText('Продолжить игру')
        self.cont_game.clicked.connect(self.continue_game)
        self.cont_game.hide()

        self.back_menu = QtWidgets.QPushButton(self.game_widget)
        self.back_menu.setGeometry(QtCore.QRect(800, 550, 281, 71))
        self.back_menu.setFont(font)
        self.back_menu.setStyleSheet("color: rgb(255, 255, 255);")
        self.back_menu.setObjectName("back_menu")
        self.back_menu.setFlat(True)
        self.back_menu.setText('Вернуться в\nглавное меню')
        self.back_menu.clicked.connect(self.back_main)
        self.back_menu.hide()


        self.rules_menu = QtWidgets.QPushButton(self.game_widget)
        self.rules_menu.setGeometry(QtCore.QRect(610, 590, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.rules_menu.setFont(font)
        self.rules_menu.setFlat(True)
        self.rules_menu.setText('?')
        self.rules_menu.setStyleSheet("color: rgb(255, 0, 0);")
        self.rules_menu.setObjectName("rules_menu")
        self.rules_menu.clicked.connect(self.open_Rules)
        self.rules_menu.hide()

        self.label = QtWidgets.QLabel(self.game_widget)
        self.label.setGeometry(QtCore.QRect(650, 225, 662, 692))
        self.label.setPixmap(QtGui.QPixmap("image/rules.png"))
        self.label.hide()

        self.back_rules = QtWidgets.QPushButton(self.game_widget)
        self.back_rules.setGeometry(QtCore.QRect(653, 227, 121, 51))
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
        self.back_rules.clicked.connect(self.close_Rules)
        self.back_rules.hide()
        self.task_A.clicked.connect(lambda: self.check_answer(self.task_A.text()))
        self.task_B.clicked.connect(lambda: self.check_answer(self.task_B.text()))
        self.task_C.clicked.connect(lambda: self.check_answer(self.task_C.text()))
        self.task_D.clicked.connect(lambda: self.check_answer(self.task_D.text()))
        self.current_question = None
        self.correct_answers_count = 0
        self.questions = self.load_questions_from_file("questions.txt")
        self.hint1_used = False

        self.show_question()

    def load_questions_from_file(self, filename):
        questions = {}
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(';')
                question = data[0]
                answers = data[1:]
                questions[question] = answers

        # Переставляем порядок вопросов случайным образом
        shuffled_questions = list(questions.items())
        shuffle(shuffled_questions)
        shuffled_questions = dict(shuffled_questions)

        return shuffled_questions

    def show_question(self):
        options = [self.task_A, self.task_B, self.task_C, self.task_D]
        for option in options:
            option.show()

        if not self.questions:
            # Если вопросов больше нет, завершаем игру или делаем что-то другое
            return

        question, options = next(iter(self.questions.items()))
        self.current_question = question

        if not options:
            # Если список опций пуст, пропускаем этот вопрос и показываем следующий
            del self.questions[question]
            self.show_question()
            return

        self.correct_answer = options[0]

        shuffled_options = options[:]
        shuffle(shuffled_options)

        self.vvod_task.setText(question)
        self.task_A.setText(shuffled_options[0])
        self.task_B.setText(shuffled_options[1])
        self.task_C.setText(shuffled_options[2])
        self.task_D.setText(shuffled_options[3])

        del self.questions[question]

    def check_answer(self, answer):
        if answer == self.correct_answer:
            print("Правильный ответ!")
            self.correct_answers_count += 1  # Увеличиваем счетчик правильных ответов
            self.total_money *= 2
            self.money_label.setText(f'Выигрыш: ${self.total_money}')
            if self.correct_answers_count == 10:  # Проверяем, достиг ли игрок 10 правильных ответов
                self.money_label.setText(f'Выигрыш: 1000000')
                self.win_text.show()
                self.label_set.show()
                self.back_menu.show()

            else:
                self.show_question()  # Показываем следующий вопрос

        else:
            self.label_set.show()
            self.back_menu.show()
            self.lose_text = QLabel(self)
            self.lose_text.setGeometry(765, 340, 600, 200)
            self.lose_text.setObjectName('lose_text')

            if self.total_money >= 32000:
                self.lose_text.setText('К сожалению, вы проиграли\n\n'
                                       'Ваш выигрыш: 32 000\n\n'
                                       'Правильный ответ: {}'.format(self.correct_answer))
            elif self.total_money >= 8000:
                self.lose_text.setText('К сожалению, вы проиграли\n\n'
                                       'Ваш выигрыш: 8 000\n\n'
                                       'Правильный ответ: {}'.format(self.correct_answer))
            else:
                self.lose_text.setText('К сожалению, вы проиграли\n\n'
                                       'Правильный ответ: {}'.format(self.correct_answer))

            self.lose_text.hide()
            font = QtGui.QFont()
            font.setFamily("Tahoma")
            font.setPointSize(16)
            font.setBold(True)
            font.setWeight(90)
            self.lose_text.show()
            self.lose_text.setStyleSheet("color: red;\n"
                                         "background-color: rgba(255, 255, 255, 0);")
            self.lose_text.setFont(font)

            # Подсветка правильного и неправильного ответов
            if answer == self.correct_answer:
                self.sender().setStyleSheet("background-color: green; color: white;")
            else:
                self.sender().setStyleSheet(
                                  "    color: white;\n"
                                  "    border-radius: 50px;\n"
                                  "    background-color: red;\n"
                                  "    width: 100px;\n"
                                  "    height: 58px;\n"
                                  "    clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);\n"
                                  )


    
    def continue_game(self):
        self.label_set.hide()
        self.cont_game.hide()
        self.back_menu.hide()
        self.rules_menu.hide()
        self.hint1_used = self.saved_hint1_used
        self.task_A.setEnabled(True)
        self.task_B.setEnabled(True)
        self.task_C.setEnabled(True)
        self.task_D.setEnabled(True)
        self.settings_but.setEnabled(True)
        self.button_click_sound_set.play()

    def open_Rules(self):
        self.back_rules.show()
        self.label.show()
        self.label_set.hide()
        self.cont_game.hide()
        self.back_menu.hide()
        self.rules_menu.hide()
        self.button_click_sound_set.play()
    def close_Rules(self):
        self.back_rules.hide()
        self.label.hide()
        self.label_set.show()
        self.cont_game.show()
        self.back_menu.show()
        self.rules_menu.show()
        self.button_click_sound_set.play()
    def open_set(self):
        self.label_set.show()
        self.cont_game.show()
        self.back_menu.show()
        self.rules_menu.show()
        self.saved_hint1_used = self.hint1_used

        self.task_A.setEnabled(False)
        self.task_B.setEnabled(False)
        self.task_C.setEnabled(False)
        self.task_D.setEnabled(False)
        self.settings_but.setEnabled(False)
        self.button_click_sound_set.play()


    def back_main(self):
        game_widget = MainWindow()
        self.setCentralWidget(game_widget)
        self.media_player.stop()


    def clicked_hint1(self):
        if not self.hint1_used:  # Проверяем, использовалась ли уже подсказка
            self.hint_1.setStyleSheet("QPushButton {\n"
                                      "    color: red;\n"
                                      "    border-radius: 20px; \n"
                                      "    background-color: rgb(170, 0, 255);\n"
                                      "}\n")
            self.hint_1.setEnabled(False)  # Блокировка кнопки после нажатия
            self.button_click_sound_5050.play()
            options = [self.task_A, self.task_B, self.task_C, self.task_D]
            correct_option = self.correct_answer
            incorrect_options = [option for option in options if option.text() != correct_option]
            hide_options = sample(incorrect_options, 2)
            self.button_click_sound_set.play()
            for option in hide_options:
                option.hide()
            self.hint1_used = True
    def restore_volume(self):
        self.media_player.setVolume(10)
    def clicked_hint2(self):
        self.hint_2.setStyleSheet("QPushButton {\n"
                                  "    color: red;\n"
                                  "    border-radius: 20px; \n"
                                  "    background-color: rgb(170, 0, 255);\n"
                                  "}\n")
        self.hint_2.setEnabled(False)  # Блокировка кнопки после нажатия
        self.button_click_sound_set.play()
        if random.random() < 0.7:  # 70% вероятность вывода верного ответа
            hint_answer = self.correct_answer
        else:
            incorrect_answers = [option.text() for option in [self.task_A, self.task_B, self.task_C, self.task_D] if
                                 option.text() != self.correct_answer]
            hint_answer = random.choice(incorrect_answers)

        QMessageBox.information(self, "Подсказка", f"Вероятно, правильный ответ: {hint_answer}")


    def clicked_hint3(self):
        self.hint_3.setStyleSheet("QPushButton {\n"
                                  "    color: red;\n"
                                  "    border-radius: 20px; \n"
                                  "    background-color: rgb(170, 0, 255);\n"
                                  "}\n")
        self.hint_3.setEnabled(False)  # Блокировка кнопки после нажатия
        self.button_click_sound_set.play()
        # Получаем список оставшихся вопросов
        remaining_questions = list(self.questions.keys())

        # Если остались еще вопросы, выбираем случайный из них и заменяем текущий вопрос
        new_question = choice(remaining_questions)
        options = self.questions.pop(new_question)

        # Обновляем текущий вопрос и ответ
        self.current_question = new_question
        self.correct_answer = options[0]

        # Перемешиваем варианты ответов
        shuffled_options = options[:]
        shuffle(shuffled_options)

        # Обновляем тексты кнопок с новыми вариантами ответов
        self.vvod_task.setText(new_question)
        self.task_A.setText(shuffled_options[0])
        self.task_B.setText(shuffled_options[1])
        self.task_C.setText(shuffled_options[2])
        self.task_D.setText(shuffled_options[3])

    #КЛАСС ВТОРОГО ОКНА


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
        self.school_but.clicked.connect(self.open_game)
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
        self.student_but.clicked.connect(self.open_game)
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
        self.genius_but.clicked.connect(self.open_game)
        self.label = QtWidgets.QLabel(self.level_widget)
        self.label.setGeometry(QtCore.QRect(20, 65, 1000, 900))
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


    def open_game(self):
        new_widget = GameWindow()
        self.setCentralWidget(new_widget)

    def back_to_menu(self):
        back_widget = MainWindow()
        self.setCentralWidget(back_widget)


        #КЛАСС ПРАВИЛ


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


        self.fon_menu = QtWidgets.QLabel(self.menu_widget)
        self.fon_menu.setGeometry(QtCore.QRect(670, 120, 1031, 871))
        self.fon_menu.setPixmap(QtGui.QPixmap("image/menushka.png"))
        self.fon_menu.setObjectName("fon_menu")
        self.setCentralWidget(self.menu_widget)
        self.rules_window = None

        self.label = QtWidgets.QLabel(self.menu_widget)
        self.label.setGeometry(QtCore.QRect(650, 225, 662, 692))
        self.label.setPixmap(QtGui.QPixmap("image/rules.png"))
        self.label.hide()

        self.back_rules = QtWidgets.QPushButton(self.menu_widget)
        self.back_rules.setGeometry(QtCore.QRect(653, 227, 121, 51))
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
        self.back_rules.clicked.connect(self.closeRules)
        self.back_rules.hide()


    def openRules(self):
        self.back_rules.show()
        self.label.show()
        self.start_game.setEnabled(False)
        self.rules_game.setEnabled(False)
        self.exit_game.setEnabled(False)
    def closeRules(self):
        self.back_rules.hide()
        self.label.hide()
        self.start_game.setEnabled(True)
        self.rules_game.setEnabled(True)
        self.exit_game.setEnabled(True)


    def switch_widget(self):
        sec_widget = Take_level()
        self.setCentralWidget(sec_widget)

    def close_application(self):
        reply = QMessageBox()
        reply.setWindowTitle('Закрытие приложенмя')
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