import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.exit(app.exec_())
