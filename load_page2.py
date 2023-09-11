from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
from page2 import Ui_Form
from load_page3 import Page3
import os
import cv2

class Page2(QWidget):
	def __init__(self, data=None, WinSize= []):
		super().__init__()
		self.p2 = Ui_Form()
		self.p2.setupUi(self)
		self.page3_run = Page3()
		self.p2.pushButton_approve.clicked.connect(self.ShowPage3)
		self.input_path = data
		self.current_image_index = 0
		self.annotations = []
		self.image = None
		self.screen_width = WinSize[0]
		self.screen_height = WinSize[1]

		self.image_files = sorted([f for f in os.listdir(self.input_path) if f.endswith(('.jpg', '.jpeg', '.png'))])

		self.p2.pushButton_prev.clicked.connect(self.showPreviousImage)
		self.p2.pushButton_next.clicked.connect(self.showNextImage)

		self.loadAnnotations()
		self.displayImageWithAnnotations()

	def loadAnnotations(self):
		image_path = os.path.join(self.input_path, self.image_files[self.current_image_index])
		self.image = cv2.imread(image_path)

		name, _ = self.image_files[self.current_image_index].rsplit('.', 1)
		annotation_file = os.path.join(self.input_path, f"{name}.txt")
		self.annotations = []  # Annotation bilgilerini sıfırlayın
		if os.path.exists(annotation_file):
			with open(annotation_file, 'r') as f:
				lines = f.readlines()
				for line in lines:
					parts = line.strip().split()
					if len(parts) == 5:
						class_id, x_center, y_center, width, height = map(float, parts)

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
		self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

		for annotation in self.annotations:
			x, y, w, h = annotation
			color = (0, 255, 0)  # Bounding box rengi (örneğin, yeşil)
			thickness = 2
			cv2.rectangle(self.image, (x - w // 2, y - h // 2), (x + w // 2, y + h // 2), color, thickness)

		height, width, channel = self.image.shape
		target_width = 1280
		target_height = 720

		# If no need to resizing
		if height < self.screen_height and width < self.screen_width:	# resim küçükse resize olmadan bas
			pixmap = self.convert_cvimage_to_qpixmap(self.image)
			self.p2.label_img.setPixmap(pixmap)
		elif height >= self.screen_height and width >= self.screen_width: # iki boyutu da büyükse daha büyük olanı baz alarak ekrana oturt ve diğerini oranla
			if height >= width:
				target_size = (int(target_height*(width/height)), target_height)
				scaled_image = cv2.resize(self.image, target_size)
				pixmap = self.convert_cvimage_to_qpixmap(scaled_image)
				self.p2.label_img.setPixmap(pixmap)
			else:
				target_size = (target_width, int(target_width*(height/width)))
				scaled_image = cv2.resize(self.image, target_size)
				pixmap = self.convert_cvimage_to_qpixmap(scaled_image)
				self.p2.label_img.setPixmap(pixmap)

		elif height >= self.screen_height:
			target_size = (int(target_height*(width/height)), target_height)
			scaled_image = cv2.resize(self.image, target_size)
			pixmap = self.convert_cvimage_to_qpixmap(scaled_image)
			self.p2.label_img.setPixmap(pixmap)
		elif width >= self.screen_width:
			target_size = (target_width, int(target_width*(height/width)))
			scaled_image = cv2.resize(self.image, target_size)
			pixmap = self.convert_cvimage_to_qpixmap(scaled_image)
			self.p2.label_img.setPixmap(pixmap)
		else:
			print("NO WAY")
			



		
	def convert_cvimage_to_qpixmap(self, cv_image):
		height, width, channel = cv_image.shape
		bytes_per_line = 3 * width
		q_image = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
		pixmap = QPixmap.fromImage(q_image)
		return pixmap


	def ShowPage3(self):
		self.close()
		self.page3_run.show()