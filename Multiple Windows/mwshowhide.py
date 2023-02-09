import sys
from random import randint
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


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
      self.window = AnotherWindow()
      self.button = QPushButton("Push for Window")
      self.button.clicked.connect(self.toggle_window)
      self.setCentralWidget(self.button)
   
   def toggle_window(self, checked):
      if self.window.isVisible():
         self.window.hide()
      else:
         self.window.show()
      
      
app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()