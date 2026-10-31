from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPoint, QRectF


class Board(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #2c3e50; border-radius: 8px;")

        self.start = None
        self.end = None

        self.lines = []
        self.cur_color = QColor("#e74c3c")
        self.cur_lines = 3

    def paint_table(self):
        painter = QPainter(self)

        painter.setRenderHint()

        for start, end, color, line in self.lines:
            pen = QPen(color, line, Qt.SolidLine, Qt.RoundCap)
            painter.setPen
            painter.drawLine(start, end)

        if self.start and self.end:
            temp_pen = QPen(self.cur_color, self.cur_lines, Qt.DashLine, Qt.RoundCap)
            painter.setPen(temp_pen)
            painter.drawLine(self.start. self.end)
            
