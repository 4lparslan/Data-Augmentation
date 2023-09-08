from PyQt5.QtWidgets import *
from noise import Ui_FormNoise

class NoisePage(QWidget):
    def __init__(self):
        super().__init__()
        self.noisepage = Ui_FormNoise()
        self.noisepage.setupUi(self)
