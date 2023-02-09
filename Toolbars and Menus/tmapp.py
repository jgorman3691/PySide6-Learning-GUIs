import sys

from PySide6.QtWidgets import(
   QMainWindow, QApplication,
   QLabel, QToolBar, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
   
   def __init__(self):
      super(MainWindow, self).__init__()
      
      self.setWindowTitle("My Awesome GUI App!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()