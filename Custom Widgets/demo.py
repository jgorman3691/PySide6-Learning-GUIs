import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication
from customizedbar import PowerBar


app = QApplication(sys.argv)
volume = PowerBar()
volume.show()

app.exec()