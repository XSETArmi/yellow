import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class MyUI(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Add Circle")
        self.button.clicked.connect(self.add_circle_signal) #Signal to the main window

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Circles")
        self.circles = []
        self.ui = MyUI()
        self.setCentralWidget(self.ui)
        self.ui.add_circle_signal = self.add_circle # Connect the signal to the function


    def add_circle(self):
        x = random.randint(10, self.width() - 10)
        y = random.randint(10, self.height() - 10)
        diameter = random.randint(10, 50)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = QColor(r, g, b)
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, diameter, color in self.circles:
            painter.setPen(QPen(color, 2))
            painter.setBrush(color) #Fill the circle with color
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
