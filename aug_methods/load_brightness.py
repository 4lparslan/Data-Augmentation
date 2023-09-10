from PyQt5.QtWidgets import *
from brightness import Ui_FormBrightness
from PyQt5.QtCore import pyqtSignal

class BrightPage(QWidget):
    the_signal = pyqtSignal(int,str,str)
    def __init__(self):
        super().__init__()
        self.brightpage = Ui_FormBrightness()
        self.brightpage.setupUi(self)

        self.brightpage.pushButton.clicked.connect(self.Confirmed)

    def Confirmed(self):
        parameter1 = self.brightpage.horizontalSlider_brightness.value()
        parameter2 = self.brightpage.checkBox_lighten.isChecked()
        parameter3 = self.brightpage.checkBox_darken.isChecked()
        self.the_signal.emit(parameter1, str(parameter2), str(parameter3))
        self.close()