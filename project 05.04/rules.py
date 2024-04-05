
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow




class RulesWindow(QMainWindow):
    def __init__(self):
        super(RulesWindow, self).__init__()
        self.setGeometry(0, 0, 661, 692)
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RulesWindow()

    window.show()
    sys.exit(app.exec())