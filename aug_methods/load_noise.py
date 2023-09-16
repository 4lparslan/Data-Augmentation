from PyQt5.QtWidgets import *
from noise import Ui_FormNoise
from PyQt5.QtCore import pyqtSignal
import numpy as np
import cv2
from PyQt5.QtGui import QImage
from PyQt5 import QtGui

class NoisePage(QWidget):
    the_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.noisepage = Ui_FormNoise()
        self.noisepage.setupUi(self)

        self.noisepage.pushButton.clicked.connect(self.Confirmed)
        self.noisepage.horizontalSlider.valueChanged.connect(self.UpdatePreview)

    def Confirmed(self):
        parameter = self.noisepage.horizontalSlider.value()
        self.the_signal.emit(parameter)
        self.close()

    def UpdatePreview(self):
        preview_img = cv2.imread("aug_methods/img.png")
        param = self.noisepage.horizontalSlider.value()
        
        height, width, channels = preview_img.shape
        noise = np.random.normal(0, param*10, (height, width, channels))
        preview_img = np.clip(preview_img + noise, 0, 255).astype(np.uint8)

        preview_img = cv2.cvtColor(preview_img, cv2.COLOR_BGR2RGB)

        bytes_per_line = 3 * width
        q_image = QImage(preview_img.data, width, height, bytes_per_line, QImage.Format_RGB888)

        self.noisepage.label_img.setPixmap(QtGui.QPixmap(q_image))