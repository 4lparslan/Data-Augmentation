import cv2
import numpy as np

class Blur:
	def __init__(self, kernel_size=None, image=None):
		self.kernel = kernel_size
		self.img = image

	def ApplyBlur(self):
		self.img = cv2.blur(self.img,(self.kernel, self.kernel))
		return self.img

class Flip:
	def __init__(self, image=None, horizontal=False, vertical=False, annotation=None):
		self.horizontal = horizontal
		self.vertical = vertical
		self.img = image
		self.annotation = annotation
		self.new_annotation = []
		self.height = self.img.shape[0]
		self.width = self.img.shape[1]

	def ApplyFlip(self):
		height, width, channels = self.img.shape

		if self.horizontal == "True" and self.vertical == "True":
			self.img = cv2.flip(self.img, 0)
			self.img = cv2.flip(self.img, 1)

		elif self.horizontal == "True":
			self.img = cv2.flip(self.img, 1)
		elif self.vertical == "True":
			self.img = cv2.flip(self.img, 0)

		for bbox in self.annotation:
			flipped_bbox = self.Flip_Bbox(bbox)
			self.new_annotation.append(flipped_bbox)
		
		return self.img, self.new_annotation

	def Flip_Bbox(self, bbox=None):
		flipped_bbox = bbox
		if self.horizontal == "True" and self.vertical == "True":
			flipped_bbox = [self.width - flipped_bbox[0], self.height - flipped_bbox[1], self.width - flipped_bbox[2], self.height - flipped_bbox[3]]

		elif self.horizontal == "True":
			flipped_bbox = [self.width - flipped_bbox[0], flipped_bbox[1], self.width - flipped_bbox[2], flipped_bbox[3]]
		elif self.vertical == "True":
			flipped_bbox = [flipped_bbox[0], self.height - flipped_bbox[1], flipped_bbox[2], self.height - flipped_bbox[3]]

		return flipped_bbox

class Noise:
	def __init__(self, kernel_size=None, image=None):
		self.kernel = kernel_size
		self.img = image

	def ApplyNoise(self):
		height, width, channels = self.img.shape
		noise = np.random.normal(0, self.kernel*10, (height, width, channels))
		self.img = np.clip(self.img + noise, 0, 255).astype(np.uint8)
		return self.img

class Hue:
	def __init__(self, hue_shift=None, image=None):
		self.hue_shift = hue_shift
		self.img = image

	def ApplyHue(self):
		hsv_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
		hsv_image[:,:,0] = np.clip(hsv_image[:,:,0] + self.hue_shift, 0, 255) % 180
		self.img = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)
		return self.img

class Saturation:
	def __init__(self, saturation_factor=None, image=None):
		self.saturation_factor = (saturation_factor / 100) * 2
		self.img = image

	def ApplySaturation(self):
		hsv_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
		hsv_image[:,:,1] = np.clip(hsv_image[:,:,1] * self.saturation_factor, 0, 255).astype(np.uint8)
		self.img = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
		return self.img

class Brightness:
	def __init__(self, brightness_factor=None, lighten=False, darken=False, image=None):
		self.brightness_factor = (1.0 + (brightness_factor / 100)) if lighten=='True' else (1.0 - (brightness_factor / 100))
		self.img = image

	def ApplyBrightness(self):
		self.img = np.clip(self.img * self.brightness_factor, 0, 255).astype(np.uint8)
		return self.img

class Rotate:
	def __init__(self, image=None, angle=None, annotation=None):
		self.angle = angle
		self.img = image
		self.annotation = annotation
		self.new_annotation = []
		self.height = self.img.shape[0]
		self.width = self.img.shape[1]

	def ApplyRotate(self):
		if self.angle == 90:
			self.img = cv2.rotate(self.img, cv2.ROTATE_90_CLOCKWISE)
		elif self.angle == 180:
			self.img = cv2.rotate(self.img, cv2.ROTATE_180)	
		elif self.angle == 270:
			self.img = cv2.rotate(self.img, cv2.ROTATE_90_COUNTERCLOCKWISE)	

		for bbox in self.annotation:
			rotated_bbox = self.Rotate_Bbox(bbox)
			self.new_annotation.append(rotated_bbox)

		return self.img, self.new_annotation


	def Rotate_Bbox(self, bbox):
		x_min, y_min, x_max, y_max = bbox

		if self.angle == 90:
			return [self.height - y_min , x_min, self.height - y_max, x_max]
		elif self.angle == 180:
			return [self.width - x_min , self.height - y_min, self.width - x_max, self.height - y_max]
		elif self.angle == 270:
			return [y_min, self.width - x_min, y_max, self.width - x_max]

class SensitiveRotate:
	def __init__(self, image=None, angle=None, annotation=None):
		self.angle = angle
		self.img = image
		self.annotation = annotation
		self.new_annotation = []
		self.height = self.img.shape[0]
		self.width = self.img.shape[1]

	def ApplySensitiveRotate(self):
		(cX, cY) = (self.width // 2, self.height // 2)
		M = cv2.getRotationMatrix2D((cX, cY), self.angle, 1.0)
		self.img = cv2.warpAffine(self.img, M, (self.width, self.height))

		for bbox in self.annotation:
			rotated_bbox = self.Sensitive_Rotate_Bbox(bbox)
			self.new_annotation.append(rotated_bbox)
		return self.img, self.new_annotation

	def Sensitive_Rotate_Bbox(self, bbox):
		angle_rad = np.radians(-self.angle)
		x_min, y_min, x_max, y_max = bbox
		bbox_w = x_max-x_min
		bbox_h = y_max-y_min
		
		#a1 = [x_min, y_min]
		#a2 = [x_max, y_min]
		#a3 = [x_min, y_max]
		#a4 = [x_max, y_max]
		
		image_center = (self.width / 2, self.height / 2)
		rotation_matrix = cv2.getRotationMatrix2D(image_center, -self.angle, 1)
		
		#Rotate all points
		rotated_a1_x = int((x_min - image_center[0]) * np.cos(angle_rad) - (y_min - image_center[1]) * np.sin(angle_rad) + image_center[0])
		rotated_a1_y = int((x_min - image_center[0]) * np.sin(angle_rad) + (y_min - image_center[1]) * np.cos(angle_rad) + image_center[1])
		
		rotated_a4_x = int((x_max - image_center[0]) * np.cos(angle_rad) - (y_max - image_center[1]) * np.sin(angle_rad) + image_center[0])
		rotated_a4_y = int((x_max - image_center[0]) * np.sin(angle_rad) + (y_max - image_center[1]) * np.cos(angle_rad) + image_center[1])

		rotated_a2_x = int((x_max - image_center[0]) * np.cos(angle_rad) - (y_min - image_center[1]) * np.sin(angle_rad) + image_center[0])
		rotated_a2_y = int((x_max - image_center[0]) * np.sin(angle_rad) + (y_min - image_center[1]) * np.cos(angle_rad) + image_center[1])

		rotated_a3_x = int((x_min - image_center[0]) * np.cos(angle_rad) - (y_max - image_center[1]) * np.sin(angle_rad) + image_center[0])
		rotated_a3_y = int((x_min - image_center[0]) * np.sin(angle_rad) + (y_max - image_center[1]) * np.cos(angle_rad) + image_center[1])

		# Relocate the points
		new_x_min = min(rotated_a1_x, rotated_a2_x, rotated_a3_x, rotated_a4_x)
		new_x_max = max(rotated_a1_x, rotated_a2_x, rotated_a3_x, rotated_a4_x)
		new_y_min = min(rotated_a1_y, rotated_a2_y, rotated_a3_y, rotated_a4_y)
		new_y_max = max(rotated_a1_y, rotated_a2_y, rotated_a3_y, rotated_a4_y)

		# Check for image border breach
		new_x_min = self.CheckForBreach(new_x_min, 0)
		new_x_max = self.CheckForBreach(new_x_max, 0)
		new_y_min = self.CheckForBreach(new_y_min, 1)
		new_y_max = self.CheckForBreach(new_y_max, 1)

		return [new_x_min, new_y_min, new_x_max, new_y_max]

	def CheckForBreach(self, location, coord):
		if location < 0:
			location = 0
		elif location > self.width and coord == 0:
			location = self.width
		elif location > self.height and coord == 1:
			location = self.height
		
		return location

class Grayscale:
	def __init__(self, image=None):
		self.img = image

	def ApplyGrayscale(self):
		self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
		self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2RGB)
		return self.img
