from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QRect, QSize
from PySide6.QtGui import QPainter, QBrush, QColor, QPen, QFont
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QDial, QSizePolicy


class _Bar(QWidget):
   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      
      self.setSizePolicy(
         QSizePolicy.MinimumExpanding,
         QSizePolicy.MinimumExpanding
      )
   
   def sizeHint(self):
      return QSize(40, 120)
   
   def paintEvent(self, e):
      painter = QPainter(self)
      
      brush = QBrush()
      brush.setColor(QColor('black'))
      brush.setStyle(Qt.SolidPattern)
      rect = QRect(0, 0, painter.device().width(), painter.device().height())
      painter.fillRect(rect, brush)
      
      # Get the current state
      dial = self.parent()._dial
      vmin, vmax = dial.minimum(), dial.maximum()
      value = dial.value()
      
      boxes = 5
      padding = 5
      
      # Define our canvas
      d_height = painter.device().height() - (2 * padding)
      d_width = painter.device().width() - (2 * padding)
      
      # Draw the bars
      step_size = d_height / boxes
      bar_height = step_size * 0.6
      bar_spacer = step_size * 0.4 / 2
      
      percent = (value - vmin) / (vmax - vmin)
      n_steps = int(percent * boxes)
      brush.setColor(QColor('red'))
      for n in range(n_steps):
         rect = QRect(
            padding,
            padding + d_height - ((n + 1) * step_size) + bar_spacer,
            d_width,
            bar_height
         )
         painter.fillRect(rect, brush)
         
      painter.end()
      
   def _trigger_refresh(self):
      self.update()


class PowerBar(QWidget):
   """
   Custom Qt Widget to show a power bar a dial.
   Demonstrates a compound and custom-drawn widget
   """
   
   def __init__(self, steps=5, *args, **kwargs):
      super(PowerBar, self).__init__(*args, **kwargs)
      
      layout = QVBoxLayout()
      self._bar = _Bar()
      layout.addWidget(self._bar)
      
      self._dial = QDial()
      self._dial.valueChanged.connect(
         self._bar._trigger_refresh
      )
      
      layout.addWidget(self._dial)
      self.setLayout(layout)