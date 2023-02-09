import sys
from random import randint
from PySide6.QtWidgets import (
   QApplication,
   QMainWindow,
   QPushButton,
   QLabel,
   QVBoxLayout,
   QWidget,
)


class AnotherWindow(QWidget):
   """
   This "window" is a QWidget.  If it has no parent,
   it will appear as a free floating window.  As desired.
   """
   def __init__(self):
      super().__init__()
      layout = QVBoxLayout()
      self.label = QLabel(f"Another Window: {randint(0,100)}")
      layout.addWidget(self.label)
      self.setLayout(layout)
      
      
class MainWindow(QMainWindow):
   
   def __init__(self):
      super().__init__()
      self.window1 = AnotherWindow()
      self.window2 = AnotherWindow()
      
      lt = QVBoxLayout()
      button1 = QPushButton("Push for Window 1")
      button1.clicked.connect(self.toggle_window1)
      lt.addWidget(button1)
      
      button2 = QPushButton("Push for Window 2")
      button2.clicked.connect(self.toggle_window2)
      lt.addWidget(button2)
      
      wt = QWidget()
      wt.setLayout(lt)
      self.setCentralWidget(wt)
   
   def toggle_window1(self, checked):
      if self.window1.isVisible():
         self.window1.hide()
      else:
         self.window1.show()
   
   def toggle_window2(self, checked):
      if self.window2.isVisible():
         self.window2.hide()
      else:
         self.window2.show()

      
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()