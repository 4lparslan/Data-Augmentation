import imutils
import cv2
import numpy as np

class SensitiveRotate:
	def __init__(self, image=None, angle=None, annotation=None):
		self.angle = angle
		self.img = image
		self.annotation = annotation
		self.new_annotation = []
		self.height = self.img.shape[0]
		self.width = self.img.shape[1]

	def ApplySensitiveRotate(self):
		(cX, cY) = (self.width // 2, self.width // 2)
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
		
		x1, y1 = self.rotate_point(x_min, y_min, image_center, angle_rad)
		x2, y2 = self.rotate_point(x_max, y_min, image_center, angle_rad)
		x3, y3 = self.rotate_point(x_min, y_max, image_center, angle_rad)
		x4, y4 = self.rotate_point(x_max, y_max, image_center, angle_rad)

		rotated_x_min = int(min(x1, x2, x3, x4))
		rotated_y_min = int(min(y1, y2, y3, y4))
		rotated_x_max = int(max(x1, x2, x3, x4))
		rotated_y_max = int(max(y1, y2, y3, y4))

		return [rotated_x_min, rotated_y_min, rotated_x_max, rotated_y_max]

	def rotate_point(self, x, y, center, angle_rad):
		# Belirli bir noktayı merkeze göre döndürme
		x_rotated = np.cos(angle_rad) * (x - center[0]) - np.sin(angle_rad) * (y - center[1]) + center[0]
		y_rotated = np.sin(angle_rad) * (x - center[0]) + np.cos(angle_rad) * (y - center[1]) + center[1]
		return x_rotated, y_rotated