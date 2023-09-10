from PyQt5.QtWidgets import *
from flip import Ui_FormFlip
from PyQt5.QtCore import pyqtSignal

class FlipPage(QWidget):
    the_signal = pyqtSignal(str,str)
    def __init__(self):
        super().__init__()
        self.flippage = Ui_FormFlip()
        self.flippage.setupUi(self)

        self.flippage.pushButton.clicked.connect(self.Confirmed)
    def Confirmed(self):
        parameter1 = self.flippage.checkBox_horizontal.isChecked()
        parameter2 = self.flippage.checkBox_vertical.isChecked()
        self.the_signal.emit(str(parameter1), str(parameter2))
        self.close()