import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainW(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.w = self.width()
        self.h = self.height()
        self.button.clicked.connect(self.paint)
        self.do_paint = False
        self.circles = []

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_random_circle(qp)
            qp.end()
            self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_random_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.setPen(QColor(255, 255, 0))
        x = randint(0, self.w - 100)
        y = randint(0, self.h - self.button.height() - 100)
        d = randint(10, 100)
        self.circles.append((x, y, d))
        for c in self.circles:
            qp.drawEllipse(c[0], c[1], c[2], c[2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainW()
    ex.show()
    sys.exit(app.exec())