import sys
from PySide6.QtWidgets import (
   QMainWindow, QApplication,
   QLabel, QCheckBox, QComboBox, QListWidget,
   QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      
      self.setWindowTitle("My App")
      
      widget = QComboBox()
      widget.addItems(["One", "Two", "Three"])
      
      # The default signal from currentIndexChanged sends the index
      widget.currentIndexChanged.connect(self.index_changed)
      
      # The same signal can send a text string
      widget.currentTextChanged.connect(self.text_changed)
      
      self.setCentralWidget(widget)
   
   def index_changed(self, i: int):
      print(i)
   
   def text_changed(self, s: str):
      print(s)
      

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()