import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Load the UI from the .ui file
        self.pushButton.clicked.connect(self.add_circle)  # Connect button to function
        self.circles = []

    def add_circle(self):
        x = random.randint(10, self.width() - 10)  # Random x within bounds
        y = random.randint(10, self.height() - 10)  # Random y within bounds
        diameter = random.randint(10, 50)          # Random diameter
        self.circles.append((x, y, diameter))
        self.update()  # Trigger repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor("yellow"), 2)) #Set pen color and width

        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

