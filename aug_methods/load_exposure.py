from PyQt5.QtWidgets import *
from exposure import Ui_FormExposure

class ExposurePage(QWidget):
    def __init__(self):
        super().__init__()
        self.exposurepage = Ui_FormExposure()
        self.exposurepage.setupUi(self)
