from PyQt5.QtWidgets import *
from blur import Ui_FormBlur
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui
from PyQt5.QtGui import QImage
import cv2

class BlurPage(QWidget):
	the_signal = pyqtSignal(int)
	def __init__(self):
		super().__init__()
		self.blurpage = Ui_FormBlur()
		self.blurpage.setupUi(self)

		self.blurpage.pushButton.clicked.connect(self.Confirmed)

		self.blurpage.horizontalSlider.valueChanged.connect(self.UpdatePreview)

	def Confirmed(self):
		parameter = self.blurpage.horizontalSlider.value()
		self.the_signal.emit(parameter)
		self.close()

	def UpdatePreview(self):

		preview_img = cv2.imread("aug_methods/img.png")
		param = self.blurpage.horizontalSlider.value()
		if param!= 0:
			preview_img = cv2.blur(preview_img,(param, param))
		else:
			preview_img = preview_img
		preview_img = cv2.cvtColor(preview_img, cv2.COLOR_BGR2RGB)

		height, width, channel = preview_img.shape
		bytes_per_line = 3 * width
		q_image = QImage(preview_img.data, width, height, bytes_per_line, QImage.Format_RGB888)

		self.blurpage.label_img.setPixmap(QtGui.QPixmap(q_image))