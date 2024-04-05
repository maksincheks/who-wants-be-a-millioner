from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtCore import QUrl

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Главное окно")
        self.setGeometry(100, 100, 400, 200)

        self.player = QMediaPlayer()
        media_content = QMediaContent(QUrl.fromLocalFile("sounds/song1.mp3"))
        self.player.setMedia(media_content)

        self.timer = QTimer()
        self.timer.timeout.connect(self.play_music)
        self.timer.start(1000)  # Запустить музыку через 1 секунду

        self.button_open_second_window = QPushButton("Открыть второе окно", self)
        self.button_open_second_window.clicked.connect(self.open_second_window)

    def play_music(self):
        self.player.play()

    def open_second_window(self):
        second_window.show()

class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Второе окно")
        self.setGeometry(200, 200, 400, 200)

        self.player = QMediaPlayer()
        self.player.setMedia(QUrl.fromLocalFile("souds/song1.mp3"))
        self.player.play()

if __name__ == '__main__':
    app = QApplication([])

    main_window = MainWindow()
    second_window = SecondWindow()

    app.exec_()