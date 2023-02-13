import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QPoint, QPointF
from PySide6.QtGui import QPixmap, QPainter, QCursor, QInputEvent, QSinglePointEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget


class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      
      self.label = QLabel()
      canvas = QPixmap(400, 300)
      canvas.fill(Qt.white)
      self.label.setPixmap(canvas)
      self.setCentralWidget(self.label)
      
      self.last_x = None
      self.last_y = None
      
   def mouseMoveEvent(self, pos):
      if self.last_x is None:
         self.last_x = pos.x()
         self.last_y = pos.y()
         return
      
      canvas = self.label.pixmap()
      painter = QPainter(canvas)
      painter.drawLine(self.last_x, self.last_y, pos.x(), pos.y())
      painter.end()
      self.label.setPixmap(canvas)
      
      self.last_x = pos.x()
      self.last_y = pos.y()
      
   def mouseReleaseEvent(self, cursor):
      self.last_x = None
      self.last_y = None


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()