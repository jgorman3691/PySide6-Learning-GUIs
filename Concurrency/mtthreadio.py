import sys
import time
import traceback
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QMainWindow, QApplication
from PySide6.QtCore import QTimer, QRunnable, Slot, QThreadPool, QObject, Signal


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
      self.signals = WorkerSignals()
      
      # Add the callback to our kwargs
      self.kwargs['progress_callback'] = self.signals.progress
   
   @Slot()  # QtCore.Slot
   def run(self):
      """
      Initialize the runner function with passed self.args, self.kwargs
      """
      
      # Retrieve args/kwargs here; and fire processing using them
      try:
         result = self.fn(*self.args, **self.kwargs)
      except:
         traceback.print_exc()
         exctype, value = sys.exc_info()[:2]
         self.signals.error.emit((exctype, value, traceback.format_exc()))
      else:
         self.signals.result.emit(result)  # Returns the result of the process
      finally:
         self.signals.finished.emit()  # Done!


class WorkerSignals(QObject):
   """
   Defines the signals available from a running worker thread.
   
   Supported Signals are:
   
   finished
      no data
      
   error
      tuple (exctype, value, traceback.format_exc()) [Exception Type, Exception Value, Formatted Exception Traceback]
   
   result
      object data returned from processing, anything
   
   progress
      integer representing the percentage completion of the process
   """
   finished = Signal()  # QtCore.Signal
   error = Signal(tuple)
   result = Signal(object)
   progress = Signal(int)


class MainWindow(QMainWindow):
   def __init__(self, *args, **kwargs):
      super(MainWindow, self).__init__(*args, **kwargs)
      
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
   
   def progress_fn(self, n):
      print(f"{n}% done")
      
   def execute_this_fn(self, progress_callback):
      for n in range(5):
         time.sleep(1)
         progress_callback.emit(n*100/4)
      
      return "Done."
   
   def print_output(self, s):
      print(s)
   
   def thread_complete(self):
      print("THREAD COMPLETE!")
      
   def oh_no(self) -> None:
      # Pass the function to be executed
      worker = Worker(self.execute_this_fn)  # Any other args, kwargs are passed to the run function
      worker.signals.result.connect(self.print_output)
      worker.signals.finished.connect(self.thread_complete)
      worker.signals.progress.connect(self.progress_fn)
      
      # And...Execute
      self.threadpool.start(worker)
   
   def recurring_timer(self):
      self.counter += 1
      self.ls.setText(f"Counter: {self.counter}")


app = QApplication(sys.argv)
window = MainWindow()
app.exec()