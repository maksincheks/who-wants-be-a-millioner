import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QSoundEffect
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtGui import QMovie
from random import shuffle, sample, choice



class GameWindow(QMainWindow):
    def __init__(self, filename):
        super(GameWindow, self).__init__()
        self.correct_answer = None
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.showFullScreen()

        self.total_money = 1000

        self.game_widget = QtWidgets.QWidget(self)
        self.game_widget.setObjectName("game_widget")

        self.media_player = QMediaPlayer()
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile("sounds/main_song.mp3")))
        self.media_player.setVolume(25)
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.start(500)
        self.timer.timeout.connect(self.play_music)


        self.button_click_sound_set = QSoundEffect()
        self.button_click_sound_set.setSource(QUrl.fromLocalFile("sounds/button.wav"))
        self.button_click_sound_set.setVolume(0.15)

        self.button_click_sound_5050 = QSoundEffect()
        self.button_click_sound_5050.setSource(QUrl.fromLocalFile("sounds/hint_5050.wav"))
        self.button_click_sound_5050.setVolume(0.15)

        self.fon_main = QtWidgets.QLabel(self.game_widget)
        self.fon_main.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.fon_main.setPixmap(QtGui.QPixmap("image/fon_game.jpg"))
        self.fon_main.setObjectName('label')

        self.money_label = QtWidgets.QLabel(self.game_widget)
        self.money_label.setGeometry(1650, 130, 300, 100)
        self.money_label.setText('Выигрыш:₽0')
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
                                  "QPushButton#task_A:hover {\n"
                                  "    background-color: rgb(30, 30, 100);\n"  # Новый цвет подсветки при наведении
                                  "}\n"
                                  "QPushButton#task_A:pressed {\n"
                                  "background-color: rgb(255, 165, 0); /* Изменяем цвет при нажатии на оранжевый */\n"
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
                                  "QPushButton#task_B:hover {\n"
                                  "    background-color: rgb(30, 30, 100);\n"  # Новый цвет подсветки при наведении
                                  "}\n"
                                  "QPushButton#task_B:pressed {\n"
                                  "background-color: rgb(255, 165, 0); /* Изменяем цвет при нажатии на оранжевый */\n"
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
                                  "QPushButton#task_D:hover {\n"
                                  "    background-color: rgb(30, 30, 100);\n"  # Новый цвет подсветки при наведении
                                  "}\n"
                                  "QPushButton#task_D:pressed {\n"
                                  "background-color: rgb(255, 165, 0); /* Изменяем цвет при нажатии на оранжевый */\n"
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
                                  "QPushButton#task_C:hover {\n"
                                  "    background-color: rgb(30, 30, 100);\n"  # Новый цвет подсветки при наведении
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
                                  "color: rgb(255, 255, 255);\n"
                                  "border-radius: 20px; \n"
                                  "background-color: rgb(170, 0, 255);\n"
                                  "}\n"
                                  "QPushButton:pressed {\n"
                                  "background-color: #f39c12; /* Цвет кнопки при нажатии */\n"
                                  "}")
        self.hint_1.setIconSize(QtCore.QSize(150, 150))
        self.hint_1.setObjectName("hint_1")
        self.hint_1.setText('50/50')
        self.hint_1.clicked.connect(self.clicked_hint1)
        self.hint_2 = QtWidgets.QPushButton(self.game_widget)
        self.hint_2.setGeometry(QtCore.QRect(1500, 20, 180, 80))
        self.hint_2.setFont(font)
        self.hint_2.setStyleSheet("QPushButton {\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "border-radius: 20px; \n"
                                  "background-color: rgb(170, 0, 255);\n"
                                  "}\n"
                                  "QPushButton:pressed {\n"
                                  "background-color: #f39c12; /* Цвет кнопки при нажатии */\n"
                                  "}")
        self.hint_2.setIconSize(QtCore.QSize(150, 150))
        self.hint_2.setObjectName("hint_2")
        self.hint_2.setText('УДАЧ-\nЛИВЫЙ')
        self.hint_2.clicked.connect(self.clicked_hint2)
        self.hint_3 = QtWidgets.QPushButton(self.game_widget)
        self.hint_3.setGeometry(QtCore.QRect(1700, 20, 180, 80))
        self.hint_3.setFont(font)
        self.hint_3.setStyleSheet("QPushButton {\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "border-radius: 20px; \n"
                                  "background-color: rgb(170, 0, 255);\n"
                                  "}\n"
                                  "QPushButton:pressed {\n"
                                  "background-color: #f39c12; /* Цвет кнопки при нажатии */\n"
                                  "}")
        self.hint_3.setIconSize(QtCore.QSize(150, 150))
        self.hint_3.setObjectName("hint_3")
        self.hint_3.setText('ЗАМЕНА\nВОПРОСА')
        self.hint_3.clicked.connect(self.clicked_hint3)

        self.vvod_task = QtWidgets.QLabel(self.game_widget)
        self.vvod_task.setGeometry(QtCore.QRect(550, 150, 800, 230))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(71)
        self.vvod_task.setFont(font)
        self.vvod_task.setAlignment(QtCore.Qt.AlignCenter)
        self.vvod_task.setStyleSheet("border-radius: 40px;\n"
                                     "background-color: rgb(0, 0, 58);\n"
                                     "color: rgb(255, 255, 255);")
        self.vvod_task.setObjectName("vvod_task")
        self.setCentralWidget(self.game_widget)

        self.take_out = QtWidgets.QPushButton(self.game_widget)
        self.take_out.setGeometry(QtCore.QRect(1690, 200, 160, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(65)
        self.take_out.setFont(font)
        self.take_out.setStyleSheet("""
                    QPushButton#school_but {
                        color: white;
                        background-color: transparent;
                        border-radius: 10px;
                        padding: 10px;
                    }
                    QPushButton#school_but:hover {
                        background-color: rgba(238, 238, 238, 0.5);
                    }
                    QPushButton#school_but:pressed {
                        background-color: white;
                    }
                """)
        self.take_out.setObjectName("school_but")
        self.take_out.setText('Забрать')
        self.take_out.clicked.connect(self.take_money)

        self.take_out_text = QLabel(self.game_widget)
        self.take_out_text.setGeometry(700, 400, 600, 50)
        self.take_out_text.setObjectName('win_text')
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(100)
        self.take_out_text.setStyleSheet("color: green;\n"
                                         "background-color: rgba(255, 255, 255, 0);")
        self.take_out_text.setFont(font)


        self.win_text = QLabel(self)
        self.win_text.setGeometry(650, 400, 600, 50)
        self.win_text.setObjectName('win_text')
        self.win_text.setText('Поздравляем! Вы выиграли ₽1 000 000')
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
        self.label.setGeometry(QtCore.QRect(575, 35, 812, 1021))
        self.label.setPixmap(QtGui.QPixmap("image/rules.png"))
        self.label.hide()

        self.back_rules = QtWidgets.QPushButton(self.game_widget)
        self.back_rules.setGeometry(QtCore.QRect(577, 45, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.back_rules.setFont(font)
        self.back_rules.setStyleSheet("QPushButton {\n"
                                      "    color: black;\n"
                                      "    background-color: #B4BCC8;\n"
                                      "    border: 2px solid #B4BCC8;\n"
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
        self.filename = filename
        self.questions = self.load_questions_from_file(self.filename)
        self.hint1_used = False
        self.hint2_used = False
        self.hint3_used = False

        # Добавляем новые поля для сохранения состояния использования подсказок
        self.saved_hint1_used = False
        self.saved_hint2_used = False
        self.saved_hint3_used = False

        self.show_question()

    @staticmethod
    def load_questions_from_file(filename):
        questions = {}
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(';')
                question = data[0]
                answers = data[1:]

                # Проверяем длину вопроса и разбиваем его на несколько строк по словам при необходимости
                max_line_length = 50  # Максимальная длина строки для вопроса
                words = question.split()
                split_question = []
                current_line = ''
                for word in words:
                    if len(current_line) + len(word) <= max_line_length:
                        current_line += word + ' '
                    else:
                        split_question.append(current_line.strip())
                        current_line = word + ' '
                if current_line:
                    split_question.append(current_line.strip())
                question = '\n'.join(split_question)

                questions[question] = answers

        # Переставляем порядок вопросов случайным образом
        shuffled_questions = list(questions.items())
        shuffle(shuffled_questions)
        shuffled_questions = dict(shuffled_questions)

        return shuffled_questions
    def show_question(self):
        global question
        options = [self.task_A, self.task_B, self.task_C, self.task_D]
        for option in options:
            option.show()

        if not self.questions:
            print("Вопросов больше нет")
            return

        if hasattr(self, 'hint_text'):
            self.hint_text.hide()

        if hasattr(self, 'take_text'):
            self.take_text.hide()

        question, options = next(iter(self.questions.items()))

        if not options or len(options) < 4:
            print("Недостаточно вариантов ответа")
            self.show_question()
            return

        self.current_question = question
        self.correct_answer = options[0]

        shuffled_options = options[:]
        shuffle(shuffled_options)

        self.vvod_task.setText(question)
        self.task_A.setText(shuffled_options[0])
        self.task_B.setText(shuffled_options[1])
        self.task_C.setText(shuffled_options[2])
        self.task_D.setText(shuffled_options[3])

        del self.questions[question]

    def block_comp(self):
        self.task_A.setEnabled(False)
        self.task_B.setEnabled(False)
        self.task_C.setEnabled(False)
        self.task_D.setEnabled(False)
        self.settings_but.setEnabled(False)
        self.take_out.setEnabled(False)

    def check_answer(self, answer):
        global correct_answers_count
        if answer == self.correct_answer:
            print("Правильный ответ!")
            self.correct_answers_count += 1  # Увеличиваем счетчик правильных ответов
            self.total_money *= 2
            self.money_label.setText(f'Выигрыш: ₽{self.total_money}')
            if self.correct_answers_count == 10:  # Проверяем, достиг ли игрок 10 правильных ответов
                self.money_label.setText(f'Выигрыш: ₽1000000')
                self.win_text.show()
                self.label_set.show()
                self.back_menu.show()
                self.block_comp()
                self.hint_1.setEnabled(False)
                self.hint_2.setEnabled(False)
                self.hint_3.setEnabled(False)

            else:
                self.show_question()  # Показываем следующий вопрос

        else:
            self.label_set.show()
            self.back_menu.show()
            self.lose_text = QLabel(self)
            self.lose_text.setGeometry(765, 340, 600, 200)
            self.lose_text.setObjectName('lose_text')

            if self.total_money >= 64000:
                self.lose_text.setText('К сожалению, вы проиграли\n\n'
                                       'Ваш выигрыш: ₽64 000\n\n'
                                       'Правильный ответ: {}'.format(self.correct_answer))
                self.hint_1.setEnabled(False)
                self.hint_2.setEnabled(False)
                self.hint_3.setEnabled(False)

                self.block_comp()
            elif self.total_money >= 8000:
                self.lose_text.setText('К сожалению, вы проиграли\n\n'
                                       'Ваш выигрыш: ₽8 000\n\n'
                                       'Правильный ответ: {}'.format(self.correct_answer))
                self.block_comp()
                self.hint_1.setEnabled(False)
                self.hint_2.setEnabled(False)
                self.hint_3.setEnabled(False)
            else:
                self.lose_text.setText('К сожалению, вы проиграли\n\n'
                                       'Правильный ответ: {}'.format(self.correct_answer))
                self.block_comp()
                self.hint_1.setEnabled(False)
                self.hint_2.setEnabled(False)
                self.hint_3.setEnabled(False)

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

    def take_money(self):
        if hasattr(self, 'take_text') and self.take_text.isVisible():
            return
        if self.correct_answers_count >= 1:
            self.take_out_text.setText(f'Ваш выигрыш составил: ₽{self.total_money}')
            self.label_set.show()
            self.take_out_text.raise_()
            self.back_menu.show()
            self.block_comp()
            self.hint_1.setEnabled(False)
            self.hint_2.setEnabled(False)
            self.hint_3.setEnabled(False)
        else:
            self.take_text = QtWidgets.QLabel(self.game_widget)
            self.take_text.setGeometry(QtCore.QRect(500, 40, 700, 70))
            self.take_text.setText("Деньги забрать невозможно")
            self.take_text.setObjectName("namegame")
            font = QtGui.QFont()
            font.setFamily("Tahoma")
            font.setPointSize(13)
            font.setBold(True)
            font.setWeight(67)
            self.take_text.setFont(font)
            style = """
                            QLabel#namegame {
                                color: #333333; /* Цвет текста */
                                background-color: #f0f0f0; /* Цвет фона */
                                border: 3px solid #0066cc; /* Обводка */
                                border-radius: 10px; /* Закругление углов */
                                padding: 10px; /* Отступы внутри QLabel */
                            }
                        """
            self.take_text.setStyleSheet(style)
            self.take_text.show()
    def continue_game(self):
        self.label_set.hide()
        self.cont_game.hide()
        self.back_menu.hide()
        self.rules_menu.hide()
        self.task_A.setEnabled(True)
        self.task_B.setEnabled(True)
        self.task_C.setEnabled(True)
        self.task_D.setEnabled(True)
        self.settings_but.setEnabled(True)
        self.hint_1.setEnabled(True)
        self.hint_2.setEnabled(True)
        self.hint_3.setEnabled(True)
        self.hint1_used = self.saved_hint1_used
        self.hint2_used = self.saved_hint2_used
        self.hint3_used = self.saved_hint3_used
        self.take_out.setEnabled(True)
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
        self.hint_1.setEnabled(False)
        self.hint_2.setEnabled(False)
        self.hint_3.setEnabled(False)
        self.saved_hint1_used = self.hint1_used
        self.saved_hint2_used = self.hint2_used
        self.saved_hint3_used = self.hint3_used

        self.block_comp()
        self.button_click_sound_set.play()

    def play_music(self):
        self.media_player.play()

    def back_main(self):
        game_widget = MainWindow()
        self.setCentralWidget(game_widget)
        self.button_click_sound_set.play()
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



    def clicked_hint2(self):
        if not self.hint2_used:
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

            self.hint2_used = True

            self.hint_text = QtWidgets.QLabel(self.game_widget)
            self.hint_text.setGeometry(QtCore.QRect(500, 40, 700, 70))
            self.hint_text.setText(f"Вероятно, правильный ответ: {hint_answer}")
            self.hint_text.setObjectName("namegame")
            font = QtGui.QFont()
            font.setFamily("Tahoma")
            font.setPointSize(13)
            font.setBold(True)
            font.setWeight(67)
            self.hint_text.setFont(font)
            style = """
                QLabel#namegame {
                    color: #333333; /* Цвет текста */
                    background-color: #f0f0f0; /* Цвет фона */
                    border: 3px solid #0066cc; /* Обводка */
                    border-radius: 10px; /* Закругление углов */
                    padding: 10px; /* Отступы внутри QLabel */
                }
            """
            self.hint_text.setStyleSheet(style)
            self.hint_text.show()


    def clicked_hint3(self):
        if not self.hint3_used:
            if self.hint2_used:
                self.hint_text.hide()
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

            # Показываем все варианты ответов
            for option in [self.task_A, self.task_B, self.task_C, self.task_D]:
                option.show()

            self.hint3_used = True


class Take_level(QMainWindow):
    def __init__(self):
        super(Take_level, self).__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setStyleSheet("background-color: #c2d4db;")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        self.level_widget = QtWidgets.QWidget(self)
        self.level_widget.setObjectName("level_widget")

        self.game_window = GameWindow

        self.button_click_sound_set = QSoundEffect()
        self.button_click_sound_set.setSource(QUrl.fromLocalFile("sounds/button.wav"))
        self.button_click_sound_set.setVolume(0.15)

        self.media_player_take = QMediaPlayer()
        self.media_player_take.setMedia(QMediaContent(QUrl.fromLocalFile("sounds/main.mp3")))
        self.media_player_take.setVolume(25)
        #self.media_player_take.play()

        self.school_but = QtWidgets.QPushButton(self.level_widget)
        self.school_but.setGeometry(QtCore.QRect(50, 850, 360, 140))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.school_but.setFont(font)
        self.school_but.setStyleSheet("""
            QPushButton#school_but {
                color: black;
                background-color: transparent;
                border: 3px solid #0066cc;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton#school_but:hover {
                background-color: rgb(238, 238, 238);
            }
            QPushButton#school_but:pressed {
                background-color: white;
            }
        """)
        self.school_but.setObjectName("school_but")
        self.school_but.setText('ШКОЛЬНИК')
        self.school_but.clicked.connect(self.open_game_school)

        self.image_school = QtWidgets.QLabel(self.level_widget)
        self.image_school.setGeometry(QtCore.QRect(1200, 200, 650, 800))
        self.image_school.setPixmap(QtGui.QPixmap("image/cat_school.png"))
        self.image_school.setVisible(False)
        self.image_school.setStyleSheet("border: 5px solid #0066cc; border-radius: 15px;")

        self.school_but.enterEvent = lambda event: self.image_school.setVisible(True)
        self.school_but.leaveEvent = lambda event: self.image_school.setVisible(False)

        self.student_but = QtWidgets.QPushButton(self.level_widget)
        self.student_but.setGeometry(QtCore.QRect(250, 620, 360, 140))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.student_but.setFont(font)
        self.student_but.setStyleSheet("QPushButton {\n"
                                       "    color: black;\n"
                                       "    background-color: transparent;\n"
                                       "border: 3px solid #0066cc; \n"
                                       "border-radius: 10px;\n"
                                       " padding: 10px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "background-color: rgb(238, 238, 238); /* тёмно-белый цвет при наведении */\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: white; /* белый цвет при нажатии */\n"
                                       "}\n"
                                       "")
        self.student_but.setObjectName("student_but")
        self.student_but.setText('СТУДЕНТ')
        self.student_but.clicked.connect(self.open_game_student)

        self.image_student = QtWidgets.QLabel(self.level_widget)
        self.image_student.setGeometry(QtCore.QRect(1200, 200, 650, 800))
        self.image_student.setPixmap(QtGui.QPixmap("image/cat_student.jpg"))
        self.image_student.setVisible(False)
        self.image_student.setStyleSheet("border: 5px solid #0066cc; border-radius: 15px;")

        self.student_but.enterEvent = lambda event: self.image_student.setVisible(True)
        self.student_but.leaveEvent = lambda event: self.image_student.setVisible(False)

        self.genius_but = QtWidgets.QPushButton(self.level_widget)
        self.genius_but.setGeometry(QtCore.QRect(437, 400, 360, 140))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.genius_but.setFont(font)
        self.genius_but.setStyleSheet("QPushButton {\n"
                                      "color: black;\n"
                                      "background-color: transparent;\n"
                                      "border: 3px solid #0066cc; \n"
                                      "border-radius: 10px;\n"
                                      " padding: 10px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "background-color: rgb(238, 238, 238); /* тёмно-белый цвет при наведении */\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "background-color: white; /* белый цвет при нажатии */\n"
                                      "}\n"
                                      "")
        self.genius_but.setObjectName("genius_but")
        self.genius_but.setText('ГЕНИЙ')
        self.genius_but.clicked.connect(self.open_game_genius)

        self.image_genius = QtWidgets.QLabel(self.level_widget)
        self.image_genius.setGeometry(QtCore.QRect(1200, 200, 650, 800))
        self.image_genius.setPixmap(QtGui.QPixmap("image/cat_genius.jpg"))
        self.image_genius.setVisible(False)
        self.image_genius.setStyleSheet("border: 5px solid #0066cc; border-radius: 15px;")

        self.genius_but.enterEvent = lambda event: self.image_genius.setVisible(True)
        self.genius_but.leaveEvent = lambda event: self.image_genius.setVisible(False)

        self.back_second = QtWidgets.QPushButton(self.level_widget)
        self.back_second.setGeometry(QtCore.QRect(2, -3, 161, 61))
        self.back_second.setStyleSheet("QPushButton {\n"
                                       "border: none;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "padding-left: 5px; /* сдвигаем изображение влево при нажатии */\n"
                                       "padding-top: 5px; /* сдвигаем изображение вверх при нажатии */\n"
                                       "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/back_rules.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_second.setIcon(icon)
        self.back_second.setIconSize(QtCore.QSize(150, 100))
        self.back_second.setObjectName("back_second")
        self.setCentralWidget(self.level_widget)
        self.back_second.clicked.connect(self.back_to_menu)

        self.namegame = QtWidgets.QLabel(self.level_widget)
        self.namegame.setGeometry(QtCore.QRect(1300, 70, 550, 70))
        self.namegame.setText('Кто хочет стать миллионером?')
        self.namegame.setObjectName("namegame")
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.namegame.setFont(font)
        style = """
            QLabel#namegame {
                color: #333333; /* Цвет текста */
                background-color: #f0f0f0; /* Цвет фона */
                border: 3px solid #0066cc; /* Обводка */
                border-radius: 10px; /* Закругление углов */
                padding: 10px; /* Отступы внутри QLabel */
            }
        """
        self.namegame.setStyleSheet(style)

        self.takelevel = QtWidgets.QLabel(self.level_widget)
        self.takelevel.setGeometry(QtCore.QRect(50, 250, 750, 100))
        self.takelevel.setText('Выберите уровень сложности')
        self.takelevel.setObjectName("takelevel")
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.takelevel.setFont(font)
        style = """
             QLabel#takelevel {
                 color: #333333; /* Цвет текста */
                 background-color: #f0f0f0; /* Цвет фона */
                 border: 3px solid #0066cc; /* Обводка */
                 border-radius: 10px; /* Закругление углов */
                 padding: 10px; /* Отступы внутри QLabel */
             }
         """
        self.takelevel.setStyleSheet(style)

    def open_game_school(self, filename):
        self.button_click_sound_set.play()
        filename = "questions.txt"
        new_widget = GameWindow(filename)
        self.setCentralWidget(new_widget)
        self.media_player_take.stop()

    def open_game_student(self):
        filename = "questions1.txt"
        new_widget = GameWindow(filename)
        self.setCentralWidget(new_widget)
        self.media_player_take.stop()
        self.button_click_sound_set.play()

    def open_game_genius(self):
        filename = "questions2.txt"
        new_widget = GameWindow(filename)
        self.setCentralWidget(new_widget)
        self.media_player_take.stop()
        self.button_click_sound_set.play()

    def back_to_menu(self):
        back_widget = MainWindow()
        self.setCentralWidget(back_widget)
        self.media_player_take.stop()
        self.button_click_sound_set.play()


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

        self.button_click_sound_set = QSoundEffect()
        self.button_click_sound_set.setSource(QUrl.fromLocalFile("sounds/button.wav"))
        self.button_click_sound_set.setVolume(0.15)

        self.media_player_main = QMediaPlayer()
        self.media_player_main.setMedia(QMediaContent(QUrl.fromLocalFile("sounds/main.mp3")))
        self.media_player_main.setVolume(25)
        self.media_player_main.play()

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
                                      "    border: 3px solid #0066cc;\n"
                                      "    background-color: transparent;\n"
                                      "    border-radius: 10px; /* Добавляем скругление углов */\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #B0E0E6; /* тёмно-серый цвет при наведении */\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: #4682B4; /* Более синий цвет при нажатии */\n"
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
                                      "    border: 3px solid #0066cc;\n"
                                      "    background-color: transparent;\n"
                                      "    border-radius: 10px; /* Добавляем скругление углов */\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #B0E0E6; /* тёмно-серый цвет при наведении */\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: #4682B4; /* Более синий цвет при нажатии */\n"
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
                                      "    border: 3px solid #0066cc;\n"
                                      "    background-color: transparent;\n"
                                      "    border-radius: 10px; /* Добавляем скругление углов */\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: #B0E0E6; /* тёмно-серый цвет при наведении */\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: #4682B4; /* Более синий цвет при нажатии */\n"
                                      "}")
        self.exit_game.setText('ВЫХОД')
        self.exit_game.clicked.connect(self.close_application)

        self.start_game.raise_()
        self.rules_game.raise_()
        self.exit_game.raise_()

        self.fon_menu = QtWidgets.QLabel(self.menu_widget)
        self.fon_menu.setGeometry(QtCore.QRect(670, 120, 1031, 871))
        self.fon_menu.setPixmap(QtGui.QPixmap("image/menushka.png"))
        self.fon_menu.setObjectName("fon_menu")
        self.setCentralWidget(self.menu_widget)
        self.rules_window = None

        self.label = QtWidgets.QLabel(self.menu_widget)
        self.label.setGeometry(QtCore.QRect(575, 35, 816, 1000))
        self.label.setPixmap(QtGui.QPixmap("image/rules.png"))
        self.label.setStyleSheet("border: 3px solid #0066cc; border-radius: 3px;")
        self.label.hide()

        self.back_rules = QtWidgets.QPushButton(self.menu_widget)
        self.back_rules.setGeometry(QtCore.QRect(582, 45, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.back_rules.setFont(font)
        self.back_rules.setStyleSheet("QPushButton {\n"
                                      "    color: black;\n"
                                      "    background-color: #B4BCC8;\n"
                                      "    border: 2px solid #B4BCC8;\n"
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

        self.fon_exit = QtWidgets.QLabel(self.menu_widget)
        self.fon_exit.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.fon_exit.setPixmap(QtGui.QPixmap("image/fon_exit.jpg"))
        self.fon_exit.setObjectName("fon_exit")
        self.fon_exit.hide()

        self.exit_text = QtWidgets.QLabel(self.menu_widget)
        self.exit_text.setGeometry(QtCore.QRect(390, 220, 680, 70))
        self.exit_text.setText('Вы уверены, что хотите покинуть приложение?')
        self.exit_text.setObjectName("exit_text")
        self.exit_text.setFont(font)
        self.exit_text.hide()

        self.exit_text_yes = QtWidgets.QPushButton(self.menu_widget)
        self.exit_text_yes.setGeometry(QtCore.QRect(577, 345, 151, 51))
        self.exit_text_yes.setFont(font)
        self.exit_text_yes.setStyleSheet("QPushButton {\n"
                                         "color: black;\n"
                                         "background-color: #B4BCC8;\n"
                                         "order: 2px solid #B4BCC8;\n"
                                         "border-radius: 10px;\n"
                                         "padding: 5px 10px;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "background-color: #B3B3B3;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "background-color: #A0A0A0;\n"
                                         "}")
        self.exit_text_yes.setObjectName("exit_text_yes")
        self.exit_text_yes.setText("Покинуть")
        self.exit_text_yes.hide()

        self.exit_text_no = QtWidgets.QPushButton(self.menu_widget)
        self.exit_text_no.setGeometry(QtCore.QRect(777, 345, 151, 51))
        self.exit_text_no.setFont(font)
        self.exit_text_no.setStyleSheet('QPushButton {\n'
                                        'color: black;\n'
                                        'background-color: #B4BCC8;\n'
                                        'order: 2px solid #B4BCC8;\n'
                                        'border-radius: 10px;\n'
                                        'padding: 5px 10px;\n'
                                        '}\n'
                                        '\n'
                                        'QPushButton:hover {\n'
                                        'background-color: #B3B3B3;\n'
                                        '}\n'
                                        '\n'
                                        'QPushButton:pressed {\n'
                                        'background-color: #A0A0A0;\n'
                                        '}')
        self.exit_text_no.setObjectName("exit_text_no")
        self.exit_text_no.setText("Остаться")
        self.exit_text_no.hide()

    def openRules(self):
        self.back_rules.show()
        self.label.show()
        self.start_game.setEnabled(False)
        self.rules_game.setEnabled(False)
        self.exit_game.setEnabled(False)
        self.button_click_sound_set.play()


    def closeRules(self):
        self.back_rules.hide()
        self.label.hide()
        self.start_game.setEnabled(True)
        self.rules_game.setEnabled(True)
        self.exit_game.setEnabled(True)
        self.button_click_sound_set.play()

    def switch_widget(self):
        self.button_click_sound_set.play()
        sec_widget = Take_level()
        self.setCentralWidget(sec_widget)
        self.media_player_main.stop()

    def close_application(self):
        self.fon_exit.show()
        self.exit_text.show()
        self.exit_text_yes.show()
        self.exit_text_no.show()
        self.button_click_sound_set.play()

        def exit_game():
            sys.exit()
            self.button_click_sound_set.play()

        self.exit_text_yes.clicked.connect(exit_game)

        def continue_game():
            self.fon_exit.hide()
            self.exit_text.hide()
            self.exit_text_yes.hide()
            self.exit_text_no.hide()
            self.button_click_sound_set.play()

        self.exit_text_no.clicked.connect(continue_game)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
