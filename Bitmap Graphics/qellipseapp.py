import sys
from random import randint, choice
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt, QPoint, QRect
from PySide6.QtGui import QPainter, QPixmap, QPen, QColor, QBrush


class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      
      self.label = QLabel()
      canvas = QPixmap(400, 300)
      canvas.fill(Qt.white)
      self.label.setPixmap(canvas)
      self.setCentralWidget(self.label)
      # self.draw_something()
      self.draw_rings()
   
   def draw_something(self):
      canvas = self.label.pixmap()
      painter = QPainter(canvas)
      pen = QPen()
      pen.setWidth(3)
      pen.setColor(QColor(204, 0, 0))
      painter.setPen(pen)
      
      painter.drawEllipse(10, 10, 100, 100)
      painter.drawEllipse(10, 10, 150, 200)
      painter.drawEllipse(10, 10, 200, 300)
      painter.end()
      self.label.setPixmap(canvas)
   
   def draw_rings(self):
      canvas = self.label.pixmap()
      painter = QPainter(canvas)
      pen = QPen()
      pen.setWidth(3)
      pen.setColor(QColor(204, 0, 0))
      painter.setPen(pen)
   
      painter.drawEllipse(QPoint(100, 100), 10, 10)
      painter.drawEllipse(QPoint(100, 100), 15, 20)
      painter.drawEllipse(QPoint(100, 100), 20, 30)
      painter.drawEllipse(QPoint(100, 100), 25, 40)
      painter.drawEllipse(QPoint(100, 100), 30, 50)
      painter.drawEllipse(QPoint(100, 100), 35, 60)
      painter.end()
      self.label.setPixmap(canvas)
      

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()