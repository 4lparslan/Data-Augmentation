import cv2
import numpy as np


class Noise:
	def __init__(self, kernel_size=None, image=None):
		self.kernel = kernel_size
		self.img = image

	def ApplyNoise(self):
		height, width, channels = self.img.shape
		noise = np.random.normal(0, self.kernel*10, (height, width, channels))
		self.img = np.clip(self.img + noise, 0, 255).astype(np.uint8)
		return self.img