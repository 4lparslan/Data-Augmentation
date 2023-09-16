from PyQt5.QtWidgets import *
from sensitive_rotate import Ui_FormSensitiveRotation
from PyQt5.QtCore import pyqtSignal
import cv2
from PyQt5.QtGui import QImage
from PyQt5 import QtGui

class SensitiveRotatePage(QWidget):
    the_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.srotatepage = Ui_FormSensitiveRotation()
        self.srotatepage.setupUi(self)

        self.srotatepage.pushButton.clicked.connect(self.Confirmed)
        self.srotatepage.horizontalSlider.valueChanged.connect(self.UpdatePreview)

    def Confirmed(self):
        parameter = self.srotatepage.horizontalSlider.value()
        self.the_signal.emit(parameter)
        self.close()

    def UpdatePreview(self):
        preview_img = cv2.imread("aug_methods/img.png")
        height, width, channel = preview_img.shape
        param = self.srotatepage.horizontalSlider.value()

        (cX, cY) = (width // 2, width // 2)
        M1 = cv2.getRotationMatrix2D((cX, cY), param, 1.0)
        M2 = cv2.getRotationMatrix2D((cX, cY), -param, 1.0)
        preview_img1 = cv2.warpAffine(preview_img, M1, (width, height))
        preview_img2 = cv2.warpAffine(preview_img, M2, (width, height))

        preview_img1 = cv2.cvtColor(preview_img1, cv2.COLOR_BGR2RGB)
        preview_img2 = cv2.cvtColor(preview_img2, cv2.COLOR_BGR2RGB)

        bytes_per_line = 3 * width
        q_image1 = QImage(preview_img1.data, width, height, bytes_per_line, QImage.Format_RGB888)
        q_image2 = QImage(preview_img2.data, width, height, bytes_per_line, QImage.Format_RGB888)

        self.srotatepage.label_img_dec.setPixmap(QtGui.QPixmap(q_image1))
        self.srotatepage.label_img_inc.setPixmap(QtGui.QPixmap(q_image2))