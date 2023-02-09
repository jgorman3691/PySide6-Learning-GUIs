
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit, QVBoxLayout, QWidget)
from PySide6.QtCore import QProcess


class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      
      self.p = None
      
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
      
   def message(self, s):
      self.text.appendPlainText(s)
      
   def start_process(self):
      if self.p is None:
         self.message("Executing Process.")
         self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running
         self.p.finished.connect(self.process_finished)
         self.p.start("python.exe", ['dummyf.py'])
      # We'll run our process here.
      pass


app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec()