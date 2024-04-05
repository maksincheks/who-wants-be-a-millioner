import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from random import shuffle

class MillionaireGame(QWidget):
    def __init__(self):
        super().__init__()
        self.questions = {
            "Сколько планет в Солнечной системе?": ["6", "7", "8", "9"],
            "Как называется столица Франции?": ["Милан", "Лондон", "Париж", "Мадрид"],
            "Какой город является столицей Японии?": ["Токио", "Пекин", "Сеул", "Ханой"],
            "Как называется самая большая планета в Солнечной системе?": ["Марс", "Юпитер", "Сатурн", "Уран"],
            "Как называется преподаватель по мдк?": ["Самоделыч", "Шахта", "Ега", "Варан"],
            "Кто написал произведение 'Война и мир'?": ["Лев Толстой", "Федор Достоевский", "Антон Чехов", "Иван Тургенев"]
        }
        self.current_question = None
        self.initUI()

    def initUI(self):
        self.vvod_task = QLabel("", self)
        self.task_A = QPushButton("", self)
        self.task_B = QPushButton("", self)
        self.task_C = QPushButton("", self)
        self.task_D = QPushButton("", self)
        self.hint_button = QPushButton("50/50 подсказка", self)

        self.vvod_task.setGeometry(50, 20, 300, 30)
        self.task_A.setGeometry(50, 60, 300, 30)
        self.task_B.setGeometry(50, 100, 300, 30)
        self.task_C.setGeometry(50, 140, 300, 30)
        self.task_D.setGeometry(50, 180, 300, 30)
        self.hint_button.setGeometry(50, 220, 300, 30)

        self.setWindowTitle('Кто хочет стать миллионером?')
        self.setGeometry(100, 100, 400, 300)

        self.show_question()

    def show_question(self):
        if not self.questions:
            print("Игра окончена.")
            return

        question, options = self.questions.popitem()
        self.current_question = question
        self.correct_answer = options[0]

        shuffled_options = options[:]
        shuffle(shuffled_options)

        self.vvod_task.setText(question)
        self.task_A.setText(shuffled_options[0])
        self.task_B.setText(shuffled_options[1])
        self.task_C.setText(shuffled_options[2])
        self.task_D.setText(shuffled_options[3])

    def check_answer(self, answer):
        if answer == self.correct_answer:
            print("Правильный ответ!")
            self.show_question()  # Показываем следующий вопрос
        else:
            print("Неправильный ответ. Правильный ответ: {}".format(self.correct_answer))
            print("Игра окончена.")
            self.close()  # Закрываем окно игры

    def fifty_fifty_hint(self):
        options = [self.correct_answer]
        while len(options) < 3:
            random_option = self.questions[self.current_question][0]
            if random_option not in options:
                options.append(random_option)

        shuffle(options)
        for button, option in zip([self.task_A, self.task_B, self.task_C], options):
            button.setText(option)

    def connect_buttons(self):
        self.task_A.clicked.connect(lambda: self.check_answer(self.task_A.text()))
        self.task_B.clicked.connect(lambda: self.check_answer(self.task_B.text()))
        self.task_C.clicked.connect(lambda: self.check_answer(self.task_C.text()))
        self.task_D.clicked.connect(lambda: self.check_answer(self.task_D.text()))
        self.hint_button.clicked.connect(self.fifty_fifty_hint)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MillionaireGame()
    ex.connect_buttons()

    ex.show()
    sys.exit(app.exec_())
