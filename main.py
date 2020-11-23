import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPainter, QColor, QPolygonF


class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.run)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setPen(QColor(randint(0,255), randint(0,255), randint(0,255)))
            self.qp.setBrush(QColor(randint(0,255), randint(0,255), randint(0,255)))
            self.draw()
            self.qp.end()

    def draw(self):
        r = randint(10, 200)
        coords = (randint(0, 600), randint(0, 400))
        self.qp.drawEllipse(*coords, r, r)

    def run(self):
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Program()
    ex.show()
    sys.exit(app.exec_())
