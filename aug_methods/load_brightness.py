from PyQt5.QtWidgets import *
from brightness import Ui_FormBrightness

class BrightPage(QWidget):
    def __init__(self):
        super().__init__()
        self.brightpage = Ui_FormBrightness()
        self.brightpage.setupUi(self)
