import sys

from PySide6.QtWidgets import (
   QApplication,
   QDialog,
   QDialogButtonBox,
   QMainWindow,
   QPushButton,
   QVBoxLayout,
   QLabel,
   QMessageBox
)


class CustomDialog(QDialog):
   def __init__(self, parent=None):
      super().__init__(parent)
      
      self.setWindowTitle("HELLO!")
      
      QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
      
      self.buttonBox = QDialogButtonBox(QBtn)
      self.buttonBox.accepted.connect(self.accept)
      self.buttonBox.rejected.connect(self.reject)
      
      self.layout = QVBoxLayout()
      message = QLabel("Something happened, is that OK?")
      self.layout.addWidget(message)
      self.layout.addWidget(self.buttonBox)
      self.setLayout(self.layout)


class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      
      self.setWindowTitle("My App")
      
      button = QPushButton("Press me for a dialog!")
      button.clicked.connect(self.button_clicked)
      self.setCentralWidget(button)
      
   def button_clicked(self, s: bool):
      dlg = QMessageBox(self)
      dlg.setWindowTitle("I have a question!")
      dlg.setText("This is a question dialog")
      dlg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
      dlg.setIcon(QMessageBox.Question)
      button = dlg.exec()
      
      if button == QMessageBox.Yes:
         print("Yes!")
      else:
         print("No!")
      
      
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
