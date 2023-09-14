from PyQt5.QtWidgets import *
from brightness import Ui_FormBrightness
from PyQt5.QtCore import pyqtSignal

class BrightPage(QWidget):
    the_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.brightpage = Ui_FormBrightness()
        self.brightpage.setupUi(self)

        self.brightpage.pushButton.clicked.connect(self.Confirmed)

    def Confirmed(self):
        parameter = self.brightpage.horizontalSlider_brightness.value()
        self.the_signal.emit(parameter)
        self.close()