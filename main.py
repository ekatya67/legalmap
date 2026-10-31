import sys
from PyQt5.QtWidgets import (
    QApplication, QButtonGroup, QCheckBox, QGridLayout, QHeaderView, QLineEdit, QMainWindow, QMessageBox, QSpinBox, QTimeEdit, QWidget, 
    QVBoxLayout, QHBoxLayout, QPushButton, QStatusBar, QTableWidget, 
    QTableWidgetItem, QLabel, QCalendarWidget, QRadioButton, QGroupBox
)

class ArchiveWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Архив судебных дел")
        self.resize(800, 500)
        layout = QVBoxLayout(self)
        self.layout = QVBoxLayout(self)
        
        self.label_filter = QLabel("📅 Выберите дату для фильтрации архивных дел:")
        self.label_filter.setStyleSheet("font-weight: bold; margin-top: 5px;")
        self.layout.addWidget(self.label_filter)
        
        self.archive_calendar = QCalendarWidget()
        self.archive_calendar.setGridVisible(True)
        self.archive_calendar.clicked.connect(self.filter_by_date)
        self.layout.addWidget(self.archive_calendar)
        
        self.label_table = QLabel("📋 Список зарегистрированных дел в базе данных:")
        self.label_table.setStyleSheet("font-weight: bold; margin-top: 10px;")
        self.layout.addWidget(self.label_table)
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Номер дела", "Категория", "Статус"])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch) 
        
        self.table.cellClicked.connect(self.on_cell_clicked)
        self.layout.addWidget(self.table)
        
        self.btn_select = QPushButton("⚡ Загрузить выбранное дело на интерактивную доску")
        self.btn_select.setStyleSheet("font-weight: bold; padding: 8px; background-color: #27ae60; color: white;")
        self.layout.addWidget(self.btn_select)

        self.populate_test_data()

    def populate_test_data(self):
        # данные для теста
        test_cases = [
        ("1", "Дело № А40-1234/2026", "Гражданское", "В производстве"),
        ("2", "Дело № УГ-987/2026", "Уголовное", "В производстве"),
        ("3", "Дело № А56-7788/2025", "Арбитраж", "В архиве")
        ]
        
        self.table.setRowCount(len(test_cases))
        
        for row_idx, case in enumerate(test_cases):
            for col_idx, text in enumerate(case):
                item = QTableWidgetItem(text)
                self.table.setItem(row_idx, col_idx, item)

    def filter_by_date(self):
        selected_date = self.archive_calendar.selectedDate().toString("dd.MM.yyyy")
        print(f"Фильтрация архива по дате: {selected_date}")
        # тут sql запрос

    def on_cell_clicked(self, row, column):
        case_number = self.table.item(row, 1).text()
        print(f"Выбрана строка: {row}, Дело: {case_number}")


class LegalCaseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LegalMap — Интерактивная карта судебного дела")
        self.resize(1200, 800)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Система LegalMap готова к работе")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)

        self.left_panel = QWidget()
        self.left_layout = QVBoxLayout(self.left_panel)
        self.main_layout.addWidget(self.left_panel, stretch=1)

        self.board_panel = QWidget()
        self.board_panel.setStyleSheet("background-color: #2c3e50; border-radius: 8px;")
        self.main_layout.addWidget(self.board_panel, stretch=2)

        self.btn_open_archive = QPushButton("📁 Открыть архив дел")
        self.btn_open_archive.setStyleSheet("font-weight: bold; padding: 10px; background-color: #34495e; color: white;")
        self.btn_open_archive.clicked.connect(self.open_archive)
        self.left_layout.addWidget(self.btn_open_archive)

        self.left_layout.addStretch()

        self.archive_window = None

        self.btn_open_archive = QPushButton("📁 Открыть архив дел")
        self.btn_open_archive.setStyleSheet("font-weight: bold; padding: 10px; background-color: #34495e; color: white;")
        self.btn_open_archive.clicked.connect(self.open_archive)
        self.left_layout.addWidget(self.btn_open_archive)

        self.form_layout = QGridLayout()
        self.left_layout.addLayout(self.form_layout)

        self.lbl_case_number = QLabel("Номер дела:")
        self.txt_case_number = QLineEdit()
        self.txt_case_number.setPlaceholderText("Например, А40-1234/2026")
        self.txt_case_number.textChanged.connect(lambda text: self.status_bar.showMessage(f"Ввод номера: {text}"))
        self.form_layout.addWidget(self.lbl_case_number, 0, 0)
        self.form_layout.addWidget(self.txt_case_number, 0, 1)

        self.lbl_time = QLabel("Время суда:")
        self.time_edit = QTimeEdit()
        self.time_edit.timeChanged.connect(lambda time: self.status_bar.showMessage(f"Время изменено: {time.toString('HH:mm')}"))
        self.form_layout.addWidget(self.lbl_time, 1, 0)
        self.form_layout.addWidget(self.time_edit, 1, 1)

        self.lbl_priority = QLabel("Приоритет (1-5):")
        self.spin_priority = QSpinBox()
        self.spin_priority.setRange(1, 5)
        self.spin_priority.valueChanged.connect(lambda val: self.status_bar.showMessage(f"Приоритет дела: {val}"))
        self.form_layout.addWidget(self.lbl_priority, 2, 0)
        self.form_layout.addWidget(self.spin_priority, 2, 1)

        self.type_group_box = QGroupBox("Категория дела")
        self.type_layout = QVBoxLayout(self.type_group_box)
        
        self.radio_criminal = QRadioButton("🔴 Уголовное")
        self.radio_civil = QRadioButton("🔵 Гражданское")
        self.radio_arbitration = QRadioButton("🟢 Арбитраж")
        self.radio_civil.setChecked(True)

        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_criminal, 1)
        self.button_group.addButton(self.radio_civil, 2)
        self.button_group.addButton(self.radio_arbitration, 3)
        self.button_group.buttonClicked.connect(lambda btn: self.status_bar.showMessage(f"Выбрано: {btn.text()}"))

        self.type_layout.addWidget(self.radio_criminal)
        self.type_layout.addWidget(self.radio_civil)
        self.type_layout.addWidget(self.radio_arbitration)
        self.left_layout.addWidget(self.type_group_box)

        self.check_active = QCheckBox("Дело в производстве")
        self.check_active.setChecked(True)
        self.check_active.stateChanged.connect(lambda state: self.status_bar.showMessage("Статус: Активно" if state == 2 else "Статус: В архиве"))
        self.left_layout.addWidget(self.check_active)

        self.btn_save = QPushButton("💾 Внести в картотеку")
        self.btn_save.setStyleSheet("font-weight: bold; padding: 8px; background-color: #2e7d32; color: white;")
        self.btn_save.clicked.connect(self.save_case_locally)
        self.left_layout.addWidget(self.btn_save)

        self.left_layout.addStretch()

    def open_archive(self):
        self.status_bar.showMessage("Открытие архива судебных дел...")
        if self.archive_window is None:
            self.archive_window = ArchiveWindow()
            
        self.archive_window.show()
        self.status_bar.showMessage("Архив открыт в отдельном окне.")

    def save_case_locally(self):
        case_num = self.txt_case_number.text()
        if not case_num:
            QMessageBox.warning(self, "Ошибка", "Введите номер дела!")
            return
        
        QMessageBox.information(self, "Успех", f"Дело {case_num} готово для записи в базу!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LegalCaseApp()
    window.show()
    sys.exit(app.exec_())