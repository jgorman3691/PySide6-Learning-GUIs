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
      
      widget = QListWidget()
      widget.addItems(["One", "Two", "Three"])
      
      # In QListWidget there are two separate signals for the item, and the string
      widget.currentItemChanged.connect(self.index_changed)
      widget.currentTextChanged.connect(self.text_changed)
      
      self.setCentralWidget(widget)
   
   def index_changed(self, i): # Not an index, i is a QListWidget item
      print(i.text())
   
   def text_changed(self, s: str):
      print(s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()