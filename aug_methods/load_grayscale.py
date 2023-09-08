from PyQt5.QtWidgets import *
from grayscale import Ui_FormGrayscale

class GrayscalePage(QWidget):
    def __init__(self):
        super().__init__()
        self.grayscalepage = Ui_FormGrayscale()
        self.grayscalepage.setupUi(self)
