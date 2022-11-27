import sys
from random import choice

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, e):
        self.paint = QPainter()
        self.paint.begin(self)
        a123 = choice(range(100))
        self.paint.setBrush(QColor(choice(range(255)), choice(range(255)), choice(range(255))))
        self.paint.drawEllipse(QPoint(600, 300), a123, a123)
        self.paint.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())