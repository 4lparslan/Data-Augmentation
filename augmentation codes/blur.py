import cv2
import numpy as np

class Blur:
	def __init__(self, kernel_size=None, image=None):
		self.kernel = kernel_size
		self.img = image

	def ApplyBlur(self):
		self.img = cv2.blur(self.img,(self.kernel, self.kernel))
		return self.img
