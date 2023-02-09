import sys
import time
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QTimer, QRunnable, Slot, QThreadPool


class Worker(QRunnable):
   """
   Worker Thread

   Inherits from QRunnable to handler worker thread setup, signals, and wrap up.
   
   :param callback: The function callback to run on this worker thread.  Supplied args and kwargs
                     will be passed through to the runner
   :type callback: function
   :param args: Arguments to pass to the callback function
   :param kwargs: Keyword arguments to pass to the callback function
   """
   def __init__(self, fn, *args, **kwargs):
      super(Worker, self).__init__()
      
      # Store the constructor arguments (to be re-used for processing)
      self.fn = fn
      self.args = args
      self.kwargs = kwargs
   
   @Slot()  # QtCore.Slot
   def run(self):
      """
      Initialize the runner function with passed self.args, self.kwargs
      """
      self.fn(*self.args, **self.kwargs)


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
      
   def execute_this_fn(self):
      print("Hello!")
      
   def oh_no(self) -> None:
      worker = Worker(self.execute_this_fn)
      self.threadpool.start(worker)
   
   def recurring_timer(self):
      self.counter += 1
      self.ls.setText(f"Counter: {self.counter}")


app = QApplication(sys.argv)
window = MainWindow()
app.exec()
      