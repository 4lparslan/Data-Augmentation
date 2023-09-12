import cv2 
import numpy as np

class Rotate:
	def __init__(self, image=None, angle=None, annotation=None):
		self.process = None
		self.angle = angle
		self.img = image
		self.annotation = annotation
		self.new_annotation = []
		self.height = self.img.shape[0]
		self.width = self.img.shape[1]

		if self.angle == 90:
			self.process = cv2.ROTATE_90_CLOCKWISE
		elif self.angle == 180:
			self.process = cv2.ROTATE_180
		elif self.angle == 270:
			self.process = cv2.ROTATE_90_COUNTERCLOCKWISE

	def ApplyRotate(self):
		self.img = cv2.rotate(self.img, self.process)
		
		for bbox in self.annotation:
			rotated_bbox = self.Rotate_Bbox(bbox)
			self.new_annotation.append(rotated_bbox)

		return self.img, self.new_annotation


	def Rotate_Bbox(self, bbox):
		angle_rad = np.radians(self.angle)

		x_min, y_min, x_max, y_max = bbox

		image_center = (self.width / 2, self.height / 2)

		rotation_matrix = cv2.getRotationMatrix2D(image_center, self.angle, 1)

		rotated_x_min = int((x_min - image_center[0]) * np.cos(angle_rad) - (y_min - image_center[1]) * np.sin(angle_rad) + image_center[0])
		rotated_y_min = int((x_min - image_center[0]) * np.sin(angle_rad) + (y_min - image_center[1]) * np.cos(angle_rad) + image_center[1])
		rotated_x_max = int((x_max - image_center[0]) * np.cos(angle_rad) - (y_max - image_center[1]) * np.sin(angle_rad) + image_center[0])
		rotated_y_max = int((x_max - image_center[0]) * np.sin(angle_rad) + (y_max - image_center[1]) * np.cos(angle_rad) + image_center[1])
		
		return [rotated_x_min, rotated_y_min, rotated_x_max, rotated_y_max]