from PyQt5.QtWidgets import *
from blur import Ui_FormBlur
from PyQt5.QtCore import pyqtSignal

class BlurPage(QWidget):
    the_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.blurpage = Ui_FormBlur()
        self.blurpage.setupUi(self)

        self.blurpage.pushButton.clicked.connect(self.Confirmed)
    def Confirmed(self):
        parameter = self.blurpage.horizontalSlider.value()
        self.the_signal.emit(parameter)
        self.close()