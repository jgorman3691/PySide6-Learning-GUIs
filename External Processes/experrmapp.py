import re
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton,
                               QPlainTextEdit, QVBoxLayout, QWidget, QProgressBar)
from PySide6.QtCore import QProcess

# A regular expression, to extract the percentage(%) complete
prog_re = re.compile(r'Total Complete: ([0-9]+)(%)')


def simple_percent_parser(output):
   """
   Matches lines using the prog_re regex, returning a single integer for the process
   :param output: integer
   :return: pc_complete
   """
   m = prog_re.search(output)
   print(m.span())
   if m:
      pc_complete = m.group(1)
      return int(pc_complete)


class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      
      self.p = None
      
      self.btn = QPushButton("Execute")
      self.btn.pressed.connect(self.start_process)
      self.text = QPlainTextEdit()
      self.text.setReadOnly(True)
      
      self.progress = QProgressBar()
      self.progress.setRange(0,100)
      
      lt = QVBoxLayout()
      lt.addWidget(self.btn)
      lt.addWidget(self.progress)
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
         self.p.readyReadStandardOutput.connect(self.handle_stdout)
         self.p.readyReadStandardError.connect(self.handle_stderr)
         self.p.stateChanged.connect(self.handle_state)
         self.p.finished.connect(self.process_finished)  # Clean up once we've completed
         self.p.start("python.exe", ['dummy.py'])
   
   def handle_stderr(self):
      data = self.p.readAllStandardError()
      stderr = bytes(data).decode("utf8")
      progress = simple_percent_parser(stderr)
      if progress:
         self.progress.setValue(progress)
         print(progress)
      self.message(stderr)
   
   def handle_stdout(self):
      data = self.p.readAllStandardOutput()
      stdout = bytes(data).decode("utf8")
      self.message(stdout)
   
   def handle_state(self, state):
      states = {
         QProcess.NotRunning: 'Not running',
         QProcess.Starting: 'Starting',
         QProcess.Running: 'Running',
      }
      state_name = states[state]
      self.message(f"State changed: {state_name}")
      
   def process_finished(self):
      self.message("Process Finished.")
      self.p = None


app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec()