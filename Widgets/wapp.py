import sys
from PySide6.QtWidgets import (
   QMainWindow, QApplication,
   QLabel, QCheckBox, QComboBox, QListWidget,
   QLineEdit, QSpinBox, QDoubleSpinBox, QSlider,
   QDial
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
   def __init__(self):
      super(MainWindow, self).__init__()
      
      self.setWindowTitle("My App")
      
      widget = QDial()
      widget.setRange(-10, 100)
      widget.setSingleStep(0.5)
      
      widget.valueChanged.connect(self.value_changed)
      widget.sliderMoved.connect(self.slider_position)
      widget.sliderPressed.connect(self.slider_pressed)
      widget.sliderReleased.connect(self.slider_released)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()