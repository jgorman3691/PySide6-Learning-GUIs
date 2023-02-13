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
      self.draw_rrect()
      
   def draw_something(self):
      canvas = self.label.pixmap()
      painter = QPainter(canvas)
      pen = QPen()
      pen.setWidth(3)
      pen.setColor(QColor('#376F9F'))
      painter.setPen(pen)
      
      brush = QBrush()
      brush.setColor(QColor('#FFD141'))
      brush.setStyle(Qt.Dense1Pattern)
      painter.setBrush(brush)
      
      painter.drawRects([
         QRect(50, 50, 100, 100),
         QRect(60, 60, 150, 100),
         QRect(70, 70, 100, 150),
         QRect(80, 80, 150, 100),
         QRect(90, 90, 100, 150)
      ])
      painter.end()
      self.label.setPixmap(canvas)
      
   def draw_rrect(self):
      canvas = self.label.pixmap()
      painter = QPainter(canvas)
      pen = QPen()
      pen.setWidth(3)
      pen.setColor(QColor('#376F9F'))
      painter.setPen(pen)
      painter.drawRoundedRect(40, 40, 100, 100, 10, 10)
      painter.drawRoundedRect(80, 80, 100, 100, 10, 50)
      painter.drawRoundedRect(120, 120, 100, 100, 50, 10)
      painter.drawRoundedRect(160, 160, 100, 100, 50, 50)
      painter.end()
      self.label.setPixmap(canvas)
   
"""
      def draw_something(self):
      canvas = self.label.pixmap()
      painter = QPainter(canvas)
      pen = QPen()
      pen.setWidth(3)
      pen.setColor(QColor('#EB5160'))
      painter.setPen(pen)
      painter.drawRect(50, 50, 100, 100)
      painter.drawRect(60, 60, 150, 100)
      painter.drawRect(70, 70, 100, 150)
      painter.drawRect(80, 80, 150, 100)
      painter.drawRect(90, 90, 100, 150)
      painter.end()
      self.label.setPixmap(canvas)
"""


    

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()