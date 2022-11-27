import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tableWidget.setColumnCount(5)
        self.g = 0
        self.con = sqlite3.connect("coffee.db")
        self.cur = self.con.cursor()
        connection = sqlite3.connect('coffee.db')
        cursor = connection.execute('select * from coffees')
        self.tableWidget.setHorizontalHeaderLabels(list(map(lambda x: x[0], cursor.description)))
        self.result = self.cur.execute(f"""SELECT * FROM coffees""").fetchall()
        self.tableWidget.setRowCount(len(self.result))
        for i in self.result:
            self.tableWidget.setItem(self.g, 0, QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(self.g, 1, QTableWidgetItem(i[1]))
            self.tableWidget.setItem(self.g, 2, QTableWidgetItem(str(i[2])))
            self.tableWidget.setItem(self.g, 3, QTableWidgetItem(str(i[3])))
            self.tableWidget.setItem(self.g, 4, QTableWidgetItem(str(i[4])))
            self.tableWidget.setItem(self.g, 5, QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(self.g, 6, QTableWidgetItem(str(i[6])))
            self.g += 1
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())