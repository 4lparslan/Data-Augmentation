from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
from page2 import Ui_Form
from load_page3 import Page3
import os
import cv2

class Page2(QWidget):
	def __init__(self, data=None):
		super().__init__()
		self.p2 = Ui_Form()
		self.p2.setupUi(self)
		self.page3_run = Page3()
		self.p2.pushButton_approve.clicked.connect(self.ShowPage3)
		self.input_path = data
		self.current_image_index = 0
		self.annotations = []
		self.image = None

		self.image_files = sorted([f for f in os.listdir(self.input_path) if f.endswith(('.jpg', '.jpeg', '.png'))])
		#self.annotation_files = sorted([f for f in os.listdir(self.input_path) if f.endswith(('.txt'))])

		self.p2.pushButton_prev.clicked.connect(self.showPreviousImage)
		self.p2.pushButton_next.clicked.connect(self.showNextImage)

		self.loadAnnotations()
		self.displayImageWithAnnotations()

	def loadAnnotations(self):
		annotation_file = os.path.join(self.input_path, f"{self.image_files[self.current_image_index][:-4]}.txt")
		self.annotations = []  # Annotation bilgilerini sıfırlayın
		if os.path.exists(annotation_file):
			with open(annotation_file, 'r') as f:
				lines = f.readlines()
				for line in lines:
					parts = line.strip().split()
					if len(parts) == 5:
						class_id, x_center, y_center, width, height = map(float, parts)
						print(class_id, x_center, y_center, width, height)
						img_width, img_height = self.image.shape[1], self.image.shape[0]  # 'self.image' kullanın
						x = int(x_center * img_width)
						y = int(y_center * img_height)
						w = int(width * img_width)
						h = int(height * img_height)

						self.annotations.append((x, y, w, h))

	def showPreviousImage(self):
		if self.current_image_index > 0:
			self.current_image_index -= 1
			self.loadAnnotations()
			self.displayImageWithAnnotations()

	def showNextImage(self):
		if self.current_image_index < len(self.image_files) - 1:
			self.current_image_index += 1
			self.loadAnnotations()
			self.displayImageWithAnnotations()
		
	def displayImageWithAnnotations(self):
		image_path = os.path.join(self.input_path, self.image_files[self.current_image_index])
		self.image = cv2.imread(image_path)  # 'self.image' değişkenini burada tanımlayın

		for annotation in self.annotations:
			x, y, w, h = annotation
			color = (0, 255, 0)  # Bounding box rengi (örneğin, yeşil)
			thickness = 2
			cv2.rectangle(self.image, (x - w // 2, y - h // 2), (x + w // 2, y + h // 2), color, thickness)


		# Görüntüyü yeniden boyutlandırın
		height, width, channel = self.image.shape
		target_width, target_height = 1280, 720  # Hedef boyutu ayarlayın
		scaled_image = cv2.resize(self.image, (target_width, target_height))

		bytes_per_line = 3 * target_width
		q_image = QImage(scaled_image.data, target_width, target_height, bytes_per_line, QImage.Format_RGB888)
		pixmap = QPixmap.fromImage(q_image)
		self.p2.label_img.setPixmap(pixmap)
		



	def ShowPage3(self):
		self.close()
		self.page3_run.show()