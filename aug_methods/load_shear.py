from PyQt5.QtWidgets import *
from shear import Ui_FormShear
from PyQt5.QtCore import pyqtSignal

class ShearPage(QWidget):
    the_signal = pyqtSignal(int, int)
    def __init__(self):
        super().__init__()
        self.shearpage = Ui_FormShear()
        self.shearpage.setupUi(self)

        self.shearpage.pushButton.clicked.connect(self.Confirmed)
    def Confirmed(self):
        parameter1 = self.shearpage.horizontalSlider_horizontal.value()
        parameter2 = self.shearpage.horizontalSlider_vertical.value()
        self.the_signal.emit(parameter1, parameter2)
        self.close()