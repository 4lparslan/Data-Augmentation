from PyQt5.QtWidgets import *
from saturation import Ui_FormSaturation
from PyQt5.QtCore import pyqtSignal

class SaturationPage(QWidget):
    the_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.saturationpage = Ui_FormSaturation()
        self.saturationpage.setupUi(self)

        self.saturationpage.pushButton.clicked.connect(self.Confirmed)
    def Confirmed(self):
        parameter = self.saturationpage.horizontalSlider.value()
        self.the_signal.emit(parameter)
        self.close()