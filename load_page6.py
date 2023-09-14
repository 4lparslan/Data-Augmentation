from PyQt5.QtWidgets import *
from page6 import Ui_Form

class Page6(QWidget):
    def __init__(self):
        super().__init__()
        self.p6 = Ui_Form()
        self.p6.setupUi(self)

