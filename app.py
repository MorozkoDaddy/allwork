import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.get_data)
        self.pushButton_2.clicked.connect(self.clear_table)
    
    def get_data(self):
        print("Получение данных...")
        # Здесь должна быть логика получения данных
        # считывание данных из файла Excel через openpyxl
    
    def clear_table(self):
        print("Очистка таблицы...")
        self.tableWidget.clearContents() 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())