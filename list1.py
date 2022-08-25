from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import requests
import bdwiki
import bing
from ui_list import *

def List(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

# app = QApplication(sys.argv)
#    window = List(Ui_Dialog, QDialog)
#    app.exec_()
