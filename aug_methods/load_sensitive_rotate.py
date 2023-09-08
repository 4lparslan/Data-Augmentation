from PyQt5.QtWidgets import *
from sensitive_rotate import Ui_FormSensitiveRotation

class SensitiveRotatePage(QWidget):
    def __init__(self):
        super().__init__()
        self.srotatepage = Ui_FormSensitiveRotation()
        self.srotatepage.setupUi(self)
