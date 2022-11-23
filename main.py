import random
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic



class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('UI', self)
        self.setting = False
        self.pushButton.clicked.connect(self.cond)

    def cond(self):
        self.setting = True
        self.update()

    def paintEvent(self, event):
        if self.setting:
            qp = QPainter()
            qp.begin(self)
            self.draw_element(qp)
            qp.end()

    def draw_element(self, qp):
        qp.setBrush(QColor("Yellow"))
        x, y = random.randint(1, 600), random.randint(1, 600)
        if x >= 300:
            max_x = 600 - x
        else:
            max_x = x
        if y >= 300:
            max_y = 600 - y
        else:
            max_y = y
        r = min(max_x, max_y)
        qp.drawEllipse(x, y, r, r)
        self.setting = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    exit(app.exec())
