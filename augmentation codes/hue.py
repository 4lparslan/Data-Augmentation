import cv2
import numpy as np

class Hue:
	def __init__(self, hue_shift=None, image=None):
		self.hue_shift = hue_shift
		self.img = image

	def ApplyHue(self):
		hsv_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
		hsv_image[:,:,0] = np.clip(hsv_image[:,:,0] + self.hue_shift, 0, 255) % 180
		self.img = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)
		return self.img
