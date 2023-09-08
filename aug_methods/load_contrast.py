from PyQt5.QtWidgets import *
from contrast import Ui_FormContrast

class ContrastPage(QWidget):
    def __init__(self):
        super().__init__()
        self.contrastpage = Ui_FormContrast()
        self.contrastpage.setupUi(self)
