import cv2

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

		if self.horizontal and self.vertical:
			self.img = cv2.flip(self.img, 0)
			self.img = cv2.flip(self.img, 1)

		elif self.horizontal:
			self.img = cv2.flip(self.img, 1)
		elif self.vertical:
			self.img = cv2.flip(self.img, 0)
		else:
			return None


		for bbox in self.annotation:
			flipped_bbox = self.Flip_Bbox(bbox)
			self.new_annotation.append(flipped_bbox)
			#cv2.rectangle(self.img, (flipped_bbox[0],flipped_bbox[1]), (flipped_bbox[2],flipped_bbox[3]), (0, 255, 0), thickness=2)
		
		return self.img, self.new_annotation

	def Flip_Bbox(self, bbox=None):
	    flipped_bbox = bbox

	    if self.horizontal:
	        flipped_bbox = [self.height - flipped_bbox[2], flipped_bbox[1], self.height - flipped_bbox[0], flipped_bbox[3]]
	    if self.vertical:
	        flipped_bbox = [flipped_bbox[0], self.width - flipped_bbox[3], flipped_bbox[2], self.width - flipped_bbox[1]]

	    return flipped_bbox