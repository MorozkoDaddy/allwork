import json
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import openpyxl

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1168, 689)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(320, 50, 421, 201))
        self.tableWidget.setProperty("name", "")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0) 
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 60, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 110, 161, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1168, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "dn"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "modTs"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "usage"))
        self.pushButton.setText(_translate("MainWindow", "Получить данные"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Подключение кнопок
        self.pushButton.clicked.connect(self.load_json_data)
        self.pushButton_2.clicked.connect(self.clear_table)

    def load_json_data(self):
        # Чтение данных
        with open('exer1-interface-data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Извлечение данных 
        entries = data.get('imdata', [])

       
        self.clear_table()

        # Заполнение таблицы данными из JSON
        for index, entry in enumerate(entries):
            l1PhysIf = entry.get('l1PhysIf', {})
            attributes = l1PhysIf.get('attributes', {})

            self.tableWidget.insertRow(index)
            self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(attributes.get("id", "")))
            self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(attributes.get("dn", "")))
            self.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(attributes.get("modTs", "")))
            self.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(attributes.get("usage", "")))

    def clear_table(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())