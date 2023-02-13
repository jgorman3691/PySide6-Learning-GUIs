import sys
from pathlib import Path, WindowsPath
from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Qt
from PySide6.QtUiTools import QUiLoader


ufile = Path("C:\\Users\\jedte\\Programming\\PySide6\\Designer\\dialog_tutorial.ui")
loader = QUiLoader()
app = QApplication(sys.argv)
dialog = loader.load(ufile, None)
dialog.show()
app.exec()