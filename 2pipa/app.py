import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
import requests
from bs4 import BeautifulSoup

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('pepepopo.ui', self)
        self.show()

        self.pushButton.clicked.connect(self.get_data)
        self.pushButton_2.clicked.connect(self.clear_table)

    @pyqtSlot()
    def get_data(self):
        try:
            response = requests.get('https://ria.ru/', timeout=(60, 90))

            if response.status_code != 200:
                print(f"Не удалось получить данные. Код статуса: {response.status_code}")
                return

            soup = BeautifulSoup(response.text, 'html.parser')
            news_items = soup.find_all('a', class_='list-item__content')

            self.clear_table() 

            for row_number, news_item in enumerate(news_items):
                title = news_item.find('h2', class_='list-item__title').text.strip()
                link = news_item['href']
                description = news_item.find('p', class_='list-item__annotation').text.strip()
                time = news_item.find('time', class_='list-item__date').text.strip()

                self.tableWidget.insertRow(row_number)
                self.tableWidget.setItem(row_number, 0, QTableWidgetItem(title))
                self.tableWidget.setItem(row_number, 1, QTableWidgetItem(description))
                self.tableWidget.setItem(row_number, 2, QTableWidgetItem(time))
                self.tableWidget.setItem(row_number, 3, QTableWidgetItem(link))

        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе: {e}")
        except AttributeError as e:
            print(f"Ошибка при разборе данных: {e}")
        except Exception as e:
            print(f"Общая ошибка: {e}")

    @pyqtSlot()
    def clear_table(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())