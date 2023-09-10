from PyQt5.QtWidgets import *
from rotate import Ui_FormRotate
from PyQt5.QtCore import pyqtSignal

class RotatePage(QWidget):
    the_signal = pyqtSignal(str, str, str)
    def __init__(self):
        super().__init__()
        self.rotatepage = Ui_FormRotate()
        self.rotatepage.setupUi(self)

        self.rotatepage.pushButton.clicked.connect(self.Confirmed)
    def Confirmed(self):
        parameter1 = self.rotatepage.checkBox_clockwise.isChecked()
        parameter2 = self.rotatepage.checkBox_counter_clockwise.isChecked()
        parameter3 = self.rotatepage.checkBox_upside_down.isChecked()
        self.the_signal.emit(str(parameter1), str(parameter2), str(parameter3))
        self.close()