import sys
import time
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QTimer, QRunnable, Slot, QThreadPool


class Worker(QRunnable):
   """
   Worker Thread
   
   :param args: Arguments to make available to the runcode
   :param kwargs: Keyword arguments to make available to the runcode
   """
   def __init__(self, *args, **kwargs):
      super(Worker, self).__init__()
      self.args = args
      self.kwargs = kwargs
   
   @Slot()  # QtCore.Slot
   def run(self):
      """
      Initialize the runner function with passed self.args, self.kwargs
      """
      
      print(self.args, self.kwargs)


class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      
      self.threadpool = QThreadPool()
      print(f"Multithreading with maximum {self.threadpool.maxThreadCount()} threads.")
      
      self.counter = 0
      
      layout = QVBoxLayout()
      
      self.ls = QLabel("Start")
      bd = QPushButton("DANGER!")
      bd.pressed.connect(self.oh_no)
      
      layout.addWidget(self.ls)
      layout.addWidget(bd)
      
      wl = QWidget()
      wl.setLayout(layout)
      
      self.setCentralWidget(wl)
      
      self.show()
      
      self.timer = QTimer()
      self.timer.setInterval(1000)
      self.timer.timeout.connect(self.recurring_timer)
      self.timer.start()
      
   def oh_no(self) -> None:
      worker = Worker()
      self.threadpool.start(worker)
   
   def recurring_timer(self):
      self.counter += 1
      self.ls.setText(f"Counter: {self.counter}")


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
      