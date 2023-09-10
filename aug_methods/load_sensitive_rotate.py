from PyQt5.QtWidgets import *
from sensitive_rotate import Ui_FormSensitiveRotation
from PyQt5.QtCore import pyqtSignal

class SensitiveRotatePage(QWidget):
    the_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.srotatepage = Ui_FormSensitiveRotation()
        self.srotatepage.setupUi(self)

        self.srotatepage.pushButton.clicked.connect(self.Confirmed)
    def Confirmed(self):
        parameter = self.srotatepage.horizontalSlider.value()
        self.the_signal.emit(parameter)
        self.close()