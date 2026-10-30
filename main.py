import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QVBoxLayout, QHBoxLayout, QPushButton, QStatusBar
)

class ArchiveWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Архив судебных дел")
        self.resize(800, 500)
        layout = QVBoxLayout(self)
        # Сюда мы чуть позже добавим QTableWidget и фильтр по датам!
        
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

    def open_archive(self):
        self.status_bar.showMessage("Открытие архива судебных дел...")
        if self.archive_window is None:
            self.archive_window = ArchiveWindow()
            
        self.archive_window.show()
        self.status_bar.showMessage("Архив открыт в отдельном окне.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LegalCaseApp()
    window.show()
    sys.exit(app.exec_())