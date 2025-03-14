from email.mime import application
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTableWidget, QTableWidgetItem
from bs4 import BeautifulSoup
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 262)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 311, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 20, 111, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 90, 111, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
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
        item.setText(_translate("MainWindow", "N"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Описание"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Время"))
        self.pushButton.setText(_translate("MainWindow", "Получить данные"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить"))


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.pushButton.clicked.connect(self.parse_news)
        self.ui.pushButton_2.clicked.connect(self.clear_table)

    def parse_news(self):
        try:
            r = requests.get('https://www.9news.com.au/france')
            soup = BeautifulSoup(r.text, 'html.parser')

            # Получение главных новостей
            main_news_titles = soup.find_all('div', class_='story__headline__text')


            # Получение второстепенных новостей
            secondary_news_titles = soup.find_all('span', class_='story__headline__text')

            # Объединяем главные и второстепенные новости
            all_news_titles = main_news_titles + secondary_news_titles

            # Очищаем таблицу перед заполнением новыми данными
            self.clear_table()

            # Заполняем таблицу новостями
            for i in range(len(all_news_titles)):
                self.ui.tableWidget.insertRow(i)
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(i+1)))  # Номер записи
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(all_news_titles[i].text.strip()))  # Заголовок

        except Exception as e:
            print(f"Ошибка: {e}")

    def clear_table(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())