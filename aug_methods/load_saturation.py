from PyQt5.QtWidgets import *
from saturation import Ui_FormSaturation

class SaturationPage(QWidget):
    def __init__(self):
        super().__init__()
        self.saturationpage = Ui_FormSaturation()
        self.saturationpage.setupUi(self)
