from PyQt5.QtWidgets import *
from hue import Ui_FormHue
from PyQt5.QtCore import pyqtSignal

class HuePage(QWidget):
    the_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.huepage = Ui_FormHue()
        self.huepage.setupUi(self)

        self.huepage.pushButton.clicked.connect(self.Confirmed)
    def Confirmed(self):
        parameter = self.huepage.horizontalSlider_hue.value()
        self.the_signal.emit(parameter)
        self.close()