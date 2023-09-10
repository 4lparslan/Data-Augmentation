from PyQt5.QtWidgets import *
from contrast import Ui_FormContrast
from PyQt5.QtCore import pyqtSignal

class ContrastPage(QWidget):
    the_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.contrastpage = Ui_FormContrast()
        self.contrastpage.setupUi(self)

        self.contrastpage.pushButton.clicked.connect(self.Confirmed)
    def Confirmed(self):
        parameter = self.contrastpage.horizontalSlider_contrast.value()
        self.the_signal.emit(parameter)
        self.close()