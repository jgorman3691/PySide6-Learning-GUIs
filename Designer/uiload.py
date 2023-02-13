import sys
from pathlib import Path
from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()
app = QApplication(sys.argv)
window = loader.load("mainwindow.ui", None)
window.show()
app.exec()