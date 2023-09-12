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
		
		#Rotate all points
		rotated_a1_x = int((x_min - image_center[0]) * np.cos(angle_rad) - (y_min - image_center[1]) * np.sin(angle_rad) + image_center[0])
		rotated_a1_y = int((x_min - image_center[0]) * np.sin(angle_rad) + (y_min - image_center[1]) * np.cos(angle_rad) + image_center[1])
		
		rotated_a4_x = int((x_max - image_center[0]) * np.cos(angle_rad) - (y_max - image_center[1]) * np.sin(angle_rad) + image_center[0])
		rotated_a4_y = int((x_max - image_center[0]) * np.sin(angle_rad) + (y_max - image_center[1]) * np.cos(angle_rad) + image_center[1])

		rotated_a2_x = int((x_max - image_center[0]) * np.cos(angle_rad) - (y_min - image_center[1]) * np.sin(angle_rad) + image_center[0])
		rotated_a2_y = int((x_max - image_center[0]) * np.sin(angle_rad) + (y_min - image_center[1]) * np.cos(angle_rad) + image_center[1])

		rotated_a3_x = int((x_min - image_center[0]) * np.cos(angle_rad) - (y_max - image_center[1]) * np.sin(angle_rad) + image_center[0])
		rotated_a3_y = int((x_min - image_center[0]) * np.sin(angle_rad) + (y_max - image_center[1]) * np.cos(angle_rad) + image_center[1])

		new_x_min = min(rotated_a1_x, rotated_a2_x, rotated_a3_x, rotated_a4_x)
		new_x_max = max(rotated_a1_x, rotated_a2_x, rotated_a3_x, rotated_a4_x)
		new_y_min = min(rotated_a1_y, rotated_a2_y, rotated_a3_y, rotated_a4_y)
		new_y_max = max(rotated_a1_y, rotated_a2_y, rotated_a3_y, rotated_a4_y)

		return [new_x_min, new_y_min, new_x_max, new_y_max]