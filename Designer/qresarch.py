import sys
from pathlib import Path
from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication
from PySide6.QtGui import QIcon

penguin = Path("C:\\Users\\jedte\\Programming\\PySide6\\Toolbars and Menus\\icons\\animal-penguin.png")
monkey = Path("C:\\Users\\jedte\\Programming\\PySide6\\Toolbars and Menus\\icons\\animal-monkey.png")


class MainWindow(QMainWindow):
   
   def __init__(self):
      super().__init__()
      
      self.setWindowTitle("Hello World")
      self.button = QPushButton("My Button")
      
      icon = QIcon(penguin)
      self.button.setIcon(icon)
      self.button.clicked.connect(self.change_icon)
      
      self.setCentralWidget(self.button)
      
      self.show()
      
   def change_icon(self):
      icon = QIcon(monkey)
      self.button.setIcon(icon)


app = QApplication(sys.argv)
w = MainWindow()
app.exec()