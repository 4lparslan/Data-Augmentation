from PyQt5.QtWidgets import *
from exposure import Ui_FormExposure
from PyQt5.QtCore import pyqtSignal

class ExposurePage(QWidget):
    the_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.exposurepage = Ui_FormExposure()
        self.exposurepage.setupUi(self)

        self.exposurepage.pushButton.clicked.connect(self.Confirmed)
    def Confirmed(self):
        parameter = self.exposurepage.horizontalSlider_exposure.value()
        self.the_signal.emit(parameter)
        self.close()