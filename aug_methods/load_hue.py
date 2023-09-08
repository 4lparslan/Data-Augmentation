from PyQt5.QtWidgets import *
from hue import Ui_FormHue

class HuePage(QWidget):
    def __init__(self):
        super().__init__()
        self.huepage = Ui_FormHue()
        self.huepage.setupUi(self)
