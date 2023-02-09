import sys

from PySide6.QtWidgets import (
   QMainWindow, QApplication,
   QLabel, QToolBar, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
   
   def __init__(self):
      super(MainWindow, self).__init__()
      
      self.setWindowTitle("My Awesome GUI App!")
      
      label = QLabel("Hello!")
      label.setAlignment(Qt.AlignCenter)
      
      self.setCentralWidget(label)
      
      toolbar = QToolBar("My main toolbar")
      self.addToolBar(toolbar)
      
   def onMyToolBarButtonClick(self, s):
      print("Click", s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()