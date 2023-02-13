import sys
from pathlib import Path, WindowsPath
from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
ufile = Path("C:\\Users\\jedte\\Programming\\PySide6\\Designer\\dialog_tutorial.ui")


class MainWindow(QMainWindow):
   
   def __init__(self):
      super().__init__()
      
      btn = QPushButton("Launch Dialog")
      btn.pressed.connect(self.launch_dialog)
      
      self.setCentralWidget(btn)
   
   def launch_dialog(self):
      dialog = loader.load(ufile, None)
      result = dialog.exec()
      if result:
         print("Success!")
      else:
         print("Cancelled.")


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()