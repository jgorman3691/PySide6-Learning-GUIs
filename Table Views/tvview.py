import sys
import datetime
from datetime import date
import math
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QAbstractTableModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtGui import QColor, QBrush, QFont, QIcon


class TableModel(QAbstractTableModel):
   def __init__(self, data):
      super(TableModel, self).__init__()
      self._data = data
      
   def data(self, index, role):
      if role == Qt.DisplayRole:
         value = self._data[index.row()][index.column()]
      
         if isinstance(value, date):
            return value.strftime("%A, %B %d, %Y")
   
         if isinstance(value, float):
            return f"{value:.2f}"
   
         if isinstance(value, str):
            return f'{str(value)}'
   
         return value
      
      if role == Qt.BackgroundRole and index.column() == 2:
         return QColor('blue')
      
      if role == Qt.BackgroundRole and index.column() == 0:
         return QColor('red')
      
      if role == Qt.TextAlignmentRole:
         value = self._data[index.row()][index.column()]
         
         if isinstance(value, int) or isinstance(value, float):
            return Qt.AlignVCenter | Qt.AlignRight
         
         else:
            return Qt.AlignVCenter | Qt.AlignHCenter
   
   def rowCount(self, index):
      return len(self._data)
   
   def columnCount(self, index):
      return len(self._data[0])


class MainWindow(QMainWindow):
   def __init__(self):
      super().__init__()
      
      self.table = QTableView()
      """
      data = [
         [4, 9, 2],
         [1, 0, 0],
         [3, 5, 0],
         [3, 3, 2],
         [7, 8, 9],
      ]
      """
      data = [
         [4, 9, 2],
         [1, -1, 'hello'],
         [3.023, 5, -5],
         [3, 3, date(2017,10,1)],
         [7.555, 8, 9]
      ]
      
      self.model = TableModel(data)
      self.table.setModel(self.model)
      
      self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()