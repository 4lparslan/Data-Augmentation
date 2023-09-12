import numpy as np
import cv2


class Brightness:
	def __init__(self, brightness_factor=None, image=None):
		self.brightness_factor = (brightness_factor / 100) * 2
		self.img = image

	def ApplyBrightness(self):
		self.img = np.clip(self.img * self.brightness_factor, 0, 255).astype(np.uint8)
		return self.img

