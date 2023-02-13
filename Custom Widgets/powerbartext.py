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
      
      percent = (value - vmin) / (vmax - vmin)
      n_steps = int(percent * 5)
      
      pen = painter.pen()
      pen.setColor(QColor('red'))
      painter.setPen(pen)
      
      font = painter.font()
      font.setFamily('Times')
      font.setPointSize(18)
      painter.setFont(font)

      painter.drawText(25, 25, f"{n_steps}")
      
      #  painter.drawText(25, 25, f"{vmin}-->{value}<--{vmax}")
      
      painter.end()
      
   def _trigger_refresh(self):
      self.update()


class PowerBar(QWidget):
   """
   Custom Qt Widget to show a power bar a dial.
   Demonstrates a compound and custom-drawn widget
   """
   
   def __init__(self, seteps=5, *args, **kwargs):
      super(PowerBar, self).__init__(*args, **kwargs)
      
      layout = QVBoxLayout()
      self._bar = _Bar()
      layout.addWidget(self._bar)
      
      self._dial = QDial()
      self._dial.valueChanged.connect(self._bar._trigger_refresh)
      layout.addWidget(self._dial)
      
      self.setLayout(layout)