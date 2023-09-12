import cv2
import numpy as np


class Saturation:
	def __init__(self, saturation_factor=None, image=None):
		self.saturation_factor = (saturation_factor / 100) * 2
		self.img = image

	def ApplySaturation(self):
		hsv_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
		hsv_image[:,:,1] = np.clip(hsv_image[:,:,1] * self.saturation_factor, 0, 255).astype(np.uint8)
		self.img = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
		return self.img
