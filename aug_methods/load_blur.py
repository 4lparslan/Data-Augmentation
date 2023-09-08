from PyQt5.QtWidgets import *
from blur import Ui_FormBlur

class BlurPage(QWidget):
    def __init__(self):
        super().__init__()
        self.blurpage = Ui_FormBlur()
        self.blurpage.setupUi(self)

        self.parameter = None

        self.blurpage.pushButton.clicked.connect(self.setParameter)
    def setParameter(self):
        self.parameter = self.blurpage.horizontalSlider.value()
        self.close()