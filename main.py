import sqlite3
import sys
from PyQt5.QtWidgets import QLineEdit, QLabel, QVBoxLayout, QFormLayout, QHBoxLayout
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QComboBox


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.connection = sqlite3.connect('films_db.sqlite')
        self.cursor = self.connection.cursor()
        
        self.parameterSelection = QComboBox()
        self.parameterSelection.addItems(['Год выпуска', 'Название', 'Продолжительность'])
        
        self.queryLine = QLineEdit()
        self.queryButton = QPushButton("Найти")
        self.queryButton.clicked.connect(self.select_data)
        self.errorLabel = QLabel("")
        
        self.idEdit = QLineEdit()
        self.idEdit.setReadOnly(True)
        
        self.titleEdit = QLineEdit()
        self.titleEdit.setReadOnly(True)
        
        self.yearEdit = QLineEdit()
        self.yearEdit.setReadOnly(True)
        
        self.genreEdit = QLineEdit()
        self.genreEdit.setReadOnly(True)
        
        self.durationEdit = QLineEdit()
        self.durationEdit.setReadOnly(True)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.parameterSelection)
        main_layout.addWidget(self.queryLine)
        main_layout.addWidget(self.queryButton)

        form_layout = QFormLayout()
        form_layout.addRow("ID:", self.idEdit)
        form_layout.addRow("Название:", self.titleEdit)
        form_layout.addRow("Год выпуска:", self.yearEdit)
        form_layout.addRow("Жанр:", self.genreEdit)
        form_layout.addRow("Продолжительность:", self.durationEdit)

        ver_layout = QVBoxLayout()
        ver_layout.addLayout(main_layout)
        ver_layout.addLayout(form_layout)
        ver_layout.addWidget(self.errorLabel)
        
        self.setLayout(ver_layout)

    def select_data(self):
        self.errorLabel.setText("")
        self.idEdit.setText("")
        self.titleEdit.setText("")
        self.yearEdit.setText("")
        self.genreEdit.setText("")
        self.durationEdit.setText("")

        parametr = self.parameterSelection.currentText()

        try:
            search = self.queryLine.text()

            if not search.strip():
                self.errorLabel("Неправильный запрос")
                return
            if parametr == "Год выпуска":
                query = "SELECT id, title, year, genre, duration FROM films WHERE year = ?"
                result = self.cursor.execute(query, (search,)).fetchone()
            elif parametr == "Название":
                query = "SELECT id, title, year, genre, duration FROM films WHERE title = ?"
                result = self.cursor.execute(query, (search,)).fetchone()
            elif parametr == "Продолжительность":
                query = "SELECT id, title, year, genre, duration FROM films WHERE duration = ?"
                result = self.cursor.execute(query, (search,)).fetchone()
            
            if result:
                self.idEdit.setText(str(result[0]))
                self.titleEdit.setText(result[1])
                self.yearEdit.setText(str(result[2]))
                self.genreEdit.setText(str(result[3]))
                self.durationEdit.setText(str(result[4]))
            else:
                self.errorLabel.setText("Ничего не найдено")
        
        except Exception:
            self.errorLabel.setText("Неправильный запрос")


if __name__ == "__main__":
    app = QApplication()
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())