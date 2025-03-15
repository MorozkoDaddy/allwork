// сбор инфы с json файла(хз какая лаба)


import sys
import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QLabel,  
    QHeaderView,  
)
from PyQt5.QtGui import QFont, QPalette, QIcon
from PyQt5.QtCore import pyqtSlot

def load_json_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"Данные из {filename}: ", data)
            return data
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return None
    except Exception as e:
        print(f"Произошла ошибка при загрузке: {str(e)}")
        return None

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("JSON Table Viewer")
        self.setGeometry(200, 200, 900, 500)
        self.setWindowIcon(QIcon("icon.png"))

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&Файл")
        open_action = file_menu.addAction("&Открыть...")
        open_action.triggered.connect(self.open_file_dialog)

        button_open = QPushButton("Открыть файл JSON")
        button_open.clicked.connect(self.open_file_dialog)
        main_layout.addWidget(button_open)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4) 
        self.table_widget.setHorizontalHeaderLabels(["Ключ", "Значение", "Имя", "ID"])  

        self.table_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  
        self.table_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)  
        self.table_widget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)  
        self.table_widget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)  

        main_layout.addWidget(self.table_widget)

        message_label = QLabel(
            "<h2>Пожалуйста, выберите файл JSON для просмотра.</h2>",
            alignment=Qt.AlignCenter,
        )
        message_label.setWordWrap(True)
        main_layout.addWidget(message_label)

    @pyqtSlot()
    def open_file_dialog(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, "Открыть файл JSON", "", "JSON файлы (*.json)"
        )
        if filename:
            self.process_json_file(filename)

    def process_json_file(self, filename):
        self.table_widget.clearContents()
        data = load_json_data(filename)
        if data is None:
            QMessageBox.warning(
                self,
                "Ошибка",
                f"Не удалось распознать информацию из файла {filename}.",
            )
            return
        self.fill_table(data)

    def fill_table(self, data):
        row_count = 0
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, dict):  
                    name = value.get('name', '')
                    _id = value.get('id', '')
                else:
                    name = ''
                    _id = ''
                self.add_row_to_table(key, str(value), name, _id, row_count)
                row_count += 1
        elif isinstance(data, list):
            for index, item in enumerate(data):
                if isinstance(item, dict):
                    name = item.get('name', '')
                    _id = item.get('id', '')
                else:
                    name = ''
                    _id = ''
                self.add_row_to_table(index, str(item), name, _id, row_count)
                row_count += 1

    def add_row_to_table(self, key, value, name, _id, row_index):
        self.table_widget.insertRow(row_index)
        key_item = QTableWidgetItem(str(key))
        value_item = QTableWidgetItem(str(value))
        name_item = QTableWidgetItem(name)
        id_item = QTableWidgetItem(_id)
        self.table_widget.setItem(row_index, 0, key_item)
        self.table_widget.setItem(row_index, 1, value_item)
        self.table_widget.setItem(row_index, 2, name_item)
        self.table_widget.setItem(row_index, 3, id_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(""" QMainWindow { background-color: white; } QLabel { font-size: 14px; word-wrap: break-word; } QPushButton { padding: 8px 16px; border-radius: 6px; background-color: #007BFF; color: white; font-weight: bold; } QPushButton:hover { background-color: #0056b3; } """)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
