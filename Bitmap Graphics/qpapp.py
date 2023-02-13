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
      # self.draw_something()
      # self.draw_point()
      # self.draw_big()
      # self.jackson_pollock_noir()
      self.jackson_pollock_vibrant()
   
   def draw_something(self):
      canvas = self.label.pixmap()
      painter = QPainter(canvas)
      painter.drawLine(10, 10, 300, 200)
      painter.end()
      self.label.setPixmap(canvas)
      
   def draw_point(self):
      canvas = self.label.pixmap()
      painter = QPainter(canvas)
      painter.drawPoint(200, 150)
      painter.end()
      self.label.setPixmap(canvas)
   
   def draw_big(self):
      canvas = self.label.pixmap()
      painter = QPainter(canvas)
      pen = QPen()
      pen.setWidth(40)
      pen.setColor(QColor('red'))
      painter.setPen(pen)
      painter.drawPoint(200, 150)
      painter.end()
      self.label.setPixmap(canvas)
   
   def jackson_pollock_noir(self):
      canvas = self.label.pixmap()
      painter = QPainter(canvas)
      pen = QPen()
      pen.setWidth(3)
      painter.setPen(pen)
      
      for n in range(10000):
         painter.drawPoint(
            200 + randint(-100, 100),
            150 + randint(-100, 100)
         )
      painter.end()
      self.label.setPixmap(canvas)
   
   def jackson_pollock_vibrant(self):
      colors = ['#FFD141', '#376F9F', '#0D1F2D', '#E9EBEF', '#EB5160']
      
      canvas = self.label.pixmap()
      painter = QPainter(canvas)
      pen = QPen()
      pen.setWidth(3)
      painter.setPen(pen)
      
      for n in range(10000):
         pen.setColor(QColor(choice(colors)))
         painter.setPen(pen)
         painter.drawPoint(
            200 + randint(-100, 100),
            150 + randint(-100, 100)
         )
      painter.end()
      self.label.setPixmap(canvas)
      
      
      

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()