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
      
      widget = QSlider(Qt.Horizontal)
      
      widget.setRange(-10, 3)
      widget.setSingleStep(3)
      
      widget.valueChanged.connect(self.value_changed)
      widget.sliderMoved.connect(self.slider_position)
      widget.sliderPressed.connect(self.slider_pressed)
      widget.sliderReleased.connect(self.slider_released)
      
      self.setCentralWidget(widget)
      
   def value_changed(self, i: int):
      print(i)
   
   def slider_position(self, p):
      print(f"Position: {p}")
   
   def slider_pressed(self):
      print("Slider pressed!")
   
   def slider_released(self):
      print("Released")
      

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()