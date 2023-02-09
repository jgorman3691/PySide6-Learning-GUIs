import sys
from pathlib import Path
from PySide6.QtWidgets import (
   QMainWindow, QApplication, QCheckBox,
   QLabel, QToolBar, QStatusBar
)
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtCore import Qt, QSize, QKeyCombination


class MainWindow(QMainWindow):
   
   def __init__(self):
      super().__init__()
      
      self.setWindowTitle("My Awesome GUI App!")
      
      label = QLabel("Hello!")
      label.setAlignment(Qt.AlignCenter)
      
      bt = "C:\\Users\\jedte\\Programming\\PySide6\\Toolbars and Menus\\icons\\bluetooth.png"
      yy = "C:\\Users\\jedte\\Programming\\PySide6\\Toolbars And Menus\\icons\\yin-yang.png"
      wg = "C:\\Users\\jedte\\Programming\\PySide6\\Toolbars And Menus\\icons\\wafer-gold.png"
      
      self.setCentralWidget(label)
      
      toolbar = QToolBar("My main toolbar")
      toolbar.setIconSize(QSize(16, 16))
      self.addToolBar(toolbar)
      
      button_action = QAction(QIcon(bt), "&Your button", self)
      button_action.setStatusTip("This is your button")
      button_action.triggered.connect(self.onMyToolBarButtonClick)
      button_action.setCheckable(True)
      button_action.setShortcut(QKeyCombination(Qt.CTRL | Qt.Key_1))
      toolbar.addAction(button_action)
      
      toolbar.addSeparator()
      
      button_action2 = QAction(QIcon(yy), "Your &button2", self)
      button_action2.setStatusTip("This is your button2")
      button_action2.triggered.connect(self.onMyToolBarButtonClick)
      button_action2.setCheckable(True)
      button_action2.setShortcut(QKeyCombination(Qt.CTRL | Qt.Key_2))
      toolbar.addAction(button_action2)
      
      toolbar.addSeparator()

      button_action3 = QAction(QIcon(wg), "Your &button3", self)
      button_action3.setStatusTip("This is your button3")
      button_action3.triggered.connect(self.onMyToolBarButtonClick)
      button_action3.setCheckable(True)
      button_action3.setShortcut(QKeyCombination(Qt.CTRL | Qt.Key_3))
      toolbar.addAction(button_action3)
      
      toolbar.addWidget(QLabel("Hello"))
      toolbar.addWidget(QCheckBox())
      
      self.setStatusBar(QStatusBar(self))
   
      menu = self.menuBar()
      file_menu = menu.addMenu("File")
      file_menu.addAction(button_action)
      file_menu.addSeparator()
      file_menu.addAction(button_action2)
      file_menu.addSeparator()
      
      file_submenu = file_menu.addMenu("Sub-Menu")
      file_submenu.addAction(button_action3)
   
   def onMyToolBarButtonClick(self, s):
      print("click", s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()