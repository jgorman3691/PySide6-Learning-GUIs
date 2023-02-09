import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit, QVBoxLayout, QWidget)
from PySide6.QtCore import QProcess


class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      
      self.btn = QPushButton("Execute")
      self.btn.pressed.connect(self.start_process)
      self.text = QPlainTextEdit()
      self.text.setReadOnly(True)
      
      lt = QVBoxLayout()
      lt.addWidget(self.btn)
      lt.addWidget(self.text)
      
      wt = QWidget()
      wt.setLayout(lt)
      
      self.setCentralWidget(wt)
      
   def start_process(self):
      # We'll run our process here.
      pass


app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec()