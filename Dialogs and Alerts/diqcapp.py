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
      
      button = QMessageBox.critical(
         self,
         "Oh dear!",
         "Something went very wrong!",
         buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
         defaultButton=QMessageBox.Discard
      )
      
      if button == QMessageBox.Discard:
         print("Discard!")
      elif button == QMessageBox.NoToAll:
         print("No to all!")
      else:
         print("Ignore!")
      
      
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
