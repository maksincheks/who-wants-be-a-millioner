import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 200, 200)
        self.setWindowTitle('First Window')

        button = QPushButton('Open Second Window', self)
        button.clicked.connect(self.openSecondWindow)

    def openSecondWindow(self):
        self.second_window = SecondWindow()
        self.second_window.show()

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Second Window')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    first_window = FirstWindow()
    first_window.show()
    sys.exit(app.exec_())