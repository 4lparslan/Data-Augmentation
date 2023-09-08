from PyQt5.QtWidgets import *
from shear import Ui_FormShear

class ShearPage(QWidget):
    def __init__(self):
        super().__init__()
        self.shearpage = Ui_FormShear()
        self.shearpage.setupUi(self)
