import sqlite3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QInputDialog, QPushButton


class SecondForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.id = 0
        self.k = 0
        self.con = sqlite3.connect("coffee.db")
        self.cur = self.con.cursor()
        self.cursor = self.con.execute('select * from coffees')
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.action.triggered.connect(self.run)
        self.action_2.triggered.connect(self.run_1)
        self.pushButton.clicked.connect(self.a)
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.lineEdit_5.hide()
        self.lineEdit_6.hide()
        self.lineEdit_7.hide()

    def a(self):
        self.fa()
        self.close()

    def run(self):
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.lineEdit_5.hide()
        self.lineEdit_6.hide()
        self.lineEdit_7.hide()
        self.k = 1
        a = list(map(lambda x: x[0], self.cursor.description))
        result = self.cur.execute(f"""SELECT {a[0]} FROM coffees""").fetchall()
        result = [str(i[0]) for i in result]
        country, ok_pressed = QInputDialog.getItem(
            self, "Выберите id", "Id изменяемого элемента",
            result, 1, False)
        if ok_pressed:
            self.id = country
            a = list(map(lambda x: x[0], self.cursor.description))[1:]
            self.label_2.show()
            self.label_3.show()
            self.label_4.show()
            self.label_5.show()
            self.label_6.show()
            self.label_7.show()
            self.lineEdit_2.show()
            self.lineEdit_3.show()
            self.lineEdit_4.show()
            self.lineEdit_5.show()
            self.lineEdit_6.show()
            self.lineEdit_7.show()
            self.label_2.setText(a[0])
            self.label_3.setText(a[1])
            self.label_4.setText(a[2])
            self.label_5.setText(a[3])
            self.label_6.setText(a[4])
            self.label_7.setText(a[5])

    def run_1(self):
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.lineEdit_5.hide()
        self.lineEdit_6.hide()
        self.lineEdit_7.hide()
        self.k = 0
        name, ok_pressed = QInputDialog.getText(self, "Введите id",
                                                "Новый id")
        if ok_pressed:
            self.id = name
            a = list(map(lambda x: x[0], self.cursor.description))[1:]
            self.label_2.show()
            self.label_3.show()
            self.label_4.show()
            self.label_5.show()
            self.label_6.show()
            self.label_7.show()
            self.lineEdit_2.show()
            self.lineEdit_3.show()
            self.lineEdit_4.show()
            self.lineEdit_5.show()
            self.lineEdit_6.show()
            self.lineEdit_7.show()
            self.label_2.setText(a[0])
            self.label_3.setText(a[1])
            self.label_4.setText(a[2])
            self.label_5.setText(a[3])
            self.label_6.setText(a[4])
            self.label_7.setText(a[5])

    def fa(self):
        if self.k == 0:
            self.cur.execute("""INSERT INTO coffees VALUES(?, ?, ?, ?, ?, ?, ?)""", (self.id, self.lineEdit_2.text(),
                                                                                self.lineEdit_3.text(),
                                                                                self.lineEdit_4.text(),
                                                                                self.lineEdit_5.text(),
                                                                                int(self.lineEdit_6.text()),
                                                                                int(self.lineEdit_7.text())))
        else:
            self.cur.execute(
                f"""UPDATE coffees SET ID = '{self.id}', 'название сорта' = '{self.lineEdit_2.text()}',
                 'степень обжарки' = '{self.lineEdit_3.text()}',
                 'молотый/в зернах' = '{self.lineEdit_4.text()}',
                  'описание вкуса' = '{self.lineEdit_5.text()}',
                   'цена' = '{self.lineEdit_6.text()}',
                    'объем упаковки' = '{self.lineEdit_7.text()}' 
                WHERE ID = {self.id} """)
        self.con.commit()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.coffee()

    def coffee(self):
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
        self.btn = QPushButton('Изменить/добавить', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(650, 10)
        self.btn.clicked.connect(self.open_second_form)

    def open_second_form(self):
        self.second_form = SecondForm()
        self.second_form.show()
        self.coffee()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
