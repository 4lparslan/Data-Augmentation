from PyQt5.QtWidgets import *
from rotate import Ui_FormRotate

class RotatePage(QWidget):
    def __init__(self):
        super().__init__()
        self.rotatepage = Ui_FormRotate()
        self.rotatepage.setupUi(self)
