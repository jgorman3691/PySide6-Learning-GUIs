import sys
from random import randint, choice
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QPixmap, QPen, QColor


class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      
      self.label = QLabel()
      canvas = QPixmap(400, 300)
      canvas.fill(Qt.white)
      self.label.setPixmap(canvas)
      self.setCentralWidget(self.label)
      self.draw_something()
   
   def draw_something(self):
      canvas = self.label.pixmap()
      painter = QPainter(canvas)
      pen = QPen()
      pen.setWidth(15)
      pen.setColor(QColor('blue'))
      painter.setPen(pen)
      painter.drawLine(
         QPoint(100, 100),
         QPoint(300, 200)
      )
      painter.end()
      self.label.setPixmap(canvas)
      

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()