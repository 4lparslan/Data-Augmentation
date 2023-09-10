from PyQt5.QtWidgets import *
from noise import Ui_FormNoise
from PyQt5.QtCore import pyqtSignal

class NoisePage(QWidget):
    the_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.noisepage = Ui_FormNoise()
        self.noisepage.setupUi(self)

        self.noisepage.pushButton.clicked.connect(self.Confirmed)
    def Confirmed(self):
        parameter = self.noisepage.horizontalSlider.value()
        self.the_signal.emit(parameter)
        self.close()