from PyQt5.QtWidgets import *
from grayscale import Ui_FormGrayscale
from PyQt5.QtCore import pyqtSignal

class GrayscalePage(QWidget):
    the_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.grayscalepage = Ui_FormGrayscale()
        self.grayscalepage.setupUi(self)

        self.grayscalepage.pushButton.clicked.connect(self.Confirmed)
    def Confirmed(self):
        parameter = self.grayscalepage.checkBox.isChecked()
        self.the_signal.emit(str(parameter))
        self.close()