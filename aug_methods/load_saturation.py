from PyQt5.QtWidgets import *
from saturation import Ui_FormSaturation
from PyQt5.QtCore import pyqtSignal
import numpy as np
import cv2
from PyQt5.QtGui import QImage
from PyQt5 import QtGui

class SaturationPage(QWidget):
    the_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.saturationpage = Ui_FormSaturation()
        self.saturationpage.setupUi(self)

        self.saturationpage.pushButton.clicked.connect(self.Confirmed)
        self.saturationpage.horizontalSlider.valueChanged.connect(self.UpdatePreview)

    def Confirmed(self):
        parameter = self.saturationpage.horizontalSlider.value()
        self.the_signal.emit(parameter)
        self.close()

    def UpdatePreview(self):
        preview_img = cv2.imread("aug_methods/img.png")
        param = self.saturationpage.horizontalSlider.value()
        param = (param / 100) * 2
        preview_img = cv2.cvtColor(preview_img, cv2.COLOR_BGR2HSV)
        preview_img[:,:,1] = np.clip(preview_img[:,:,1] * param, 0, 255).astype(np.uint8)
        preview_img = cv2.cvtColor(preview_img, cv2.COLOR_HSV2RGB)

        height, width, channel = preview_img.shape
        bytes_per_line = 3 * width
        q_image = QImage(preview_img.data, width, height, bytes_per_line, QImage.Format_RGB888)

        self.saturationpage.label_img.setPixmap(QtGui.QPixmap(q_image))

