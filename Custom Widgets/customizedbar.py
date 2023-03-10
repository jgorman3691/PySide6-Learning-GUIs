from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QRect, QSize, Signal
from PySide6.QtGui import QPainter, QBrush, QColor, QPen, QFont
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QDial, QSizePolicy


class _Bar(QWidget):
   
   clickedValue = Signal(int)
   
   def __init__(self, steps, *args, **kwargs):
      super().__init__(*args, **kwargs)
      
      self.setSizePolicy(
         QSizePolicy.MinimumExpanding,
         QSizePolicy.MinimumExpanding
      )
      
      if isinstance(steps, list):
         # List of Colors
         self.n_steps = len(steps)
         self.steps = steps
      
      elif isinstance(steps, int):
         # Int number of bars, defaults to red
         self.n_steps = steps
         self.steps = ['red'] * steps
      
      else:
         raise TypeError('Steps must be a list or an int')
      
      self._bar_solid_percent = 0.8
      self._background_color = QColor('black')
      self._padding = 4.0  # Size of gap around the edge in number of pixels
   
   def sizeHint(self):
      return QSize(40, 120)
   
   def paintEvent(self, e):
      painter = QPainter(self)
      
      brush = QBrush()
      brush.setColor(self._background_color)
      brush.setStyle(Qt.SolidPattern)
      rect = QRect(0, 0, painter.device().width(), painter.device().height())
      painter.fillRect(rect, brush)
      
      # Get the current state
      parent = self.parent()
      vmin, vmax = parent.minimum(), parent.maximum()
      value = parent.value()
      
      # Define our canvas
      d_height = painter.device().height() - (2 * self._padding)
      d_width = painter.device().width() - (2 * self._padding)
      
      # Draw the bars
      step_size = d_height / self.n_steps
      bar_height = step_size * self._bar_solid_percent
      bar_spacer = step_size * (1 - self._bar_solid_percent) / 2
      
      # Calculate the y-stop position, from the value in the range
      percent = (value - vmin) / (vmax - vmin)
      n_steps_to_draw = int(percent * self.n_steps)
      
      for n in range(n_steps_to_draw):
         brush.setColor(QColor(self.steps[n]))
         rect = QRect(
            self._padding,
            self._padding + d_height - ((n + 1) * step_size) + bar_spacer,
            d_width,
            bar_height
         )
         painter.fillRect(rect, brush)
         
      painter.end()

   def _calculate_clicked_value(self, e):
      parent = self.parent()
      vmin, vmax = parent.minimum(), parent.maximum()
      d_height = self.size().height() + (self._padding * 2)
      step_size = d_height / self.n_steps
      click_y = e.y() - self._padding - step_size / 2
      
      percent = (d_height - click_y) / d_height
      value = vmin + percent * (vmax - vmin)
      self.clickedValue.emit(value)
      
   def mouseMoveEvent(self, e):
      self._calculate_clicked_value(e)
   
   def mousePressEvent(self, e):
      self._calculate_clicked_value(e)
      
   def _trigger_refresh(self):
      self.update()


class PowerBar(QWidget):
   """
   Custom Qt Widget to show a power bar a dial.
   Demonstrates a compound and custom-drawn widget
   
   Left-Clicking the button shows the color-chooser, while
   right-clicking resets the color to None (no-color).
   """
   
   colorChanged = Signal()
   
   def __init__(self, steps=5, *args, **kwargs):
      super(PowerBar, self).__init__(*args, **kwargs)
      
      layout = QVBoxLayout()
      self._bar = _Bar(steps)
      layout.addWidget(self._bar)
      
      # Create the QDial widget and set up the defaults.
      # We provide accessors on this class to override
      self._dial = QDial()
      self._dial.setNotchesVisible(True)
      self._dial.setWrapping(False)
      self._dial.valueChanged.connect(
         self._bar._trigger_refresh
      )
      
      # Take feedback from click events on the meter.
      self._bar.clickedValue.connect(self._dial.setValue)
      
      layout.addWidget(self._dial)
      self.setLayout(layout)

   def __getattr__(self, name):
      if name in self.__dict__:
         return self[name]
      return getattr(self._dial, name)
      
   def setColor(self, color):
      self._bar.steps = [color] * self._bar.n_steps
      self._bar.update()
   
   def setColors(self, colors):
      self._bar.n_steps = len(colors)
      self._bar.steps = colors
      self._bar.update()
   
   def setBarPadding(self, i):
      self._bar._padding = int(i)
      self._bar._update()
   
   def setBarSolidPercent(self, f):
      self._bar._bar_solid_percent = float(f)
      self._bar.update()
   
   def setBackgroundColor(self, color):
      self._bar._barckground_color = QColor(color)
      self._bar._update()
   
   def setBarCount(self, i):
      self._bar.n_steps = int(i)
      self._bar._update()