from PySide6.QtCore import Property, QObject, Signal


class CustomObject(QObject):
   
   valueChanged = Signal(int)
   
   def __init__(self):
      super().__init__()
      self._value = 0      # The default value
   
   # Change the setter function to be as:
   @value.setter
   def value(self, value):
      # Here, the check is EXTREMELY important to prevent
      # excess signals from spamming the system
      if value != self._value:
         self._value = value
         self.valueChanged.emit(value)