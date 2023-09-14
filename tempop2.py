import os
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5 import QtCore


class ObjectDetectionViewer(QMainWindow):
    def __init__(self, image_folder, annotation_folder):
        super().__init__()

        self.image_folder = image_folder
        self.annotation_folder = annotation_folder
        self.image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))])
        self.current_image_index = 0
        self.annotations = []

        #first_im = os.path.join(self.image_folder, self.image_files[self.current_image_index])
        #self.image = cv2.imread(first_im)

        self.initUI()
        self.loadAnnotations()
        self.displayImageWithAnnotations()

    def initUI(self):
        self.setWindowTitle('Nesne Tespiti Görüntüleyici')
        self.setGeometry(100, 100, 1280, 720)  # Pencere boyutunu 1920x1080 olarak ayarlayın

        self.image_label = QLabel(self)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.prev_button = QPushButton('Önceki Resim', self)
        self.prev_button.clicked.connect(self.showPreviousImage)

        self.next_button = QPushButton('Sonraki Resim', self)
        self.next_button.clicked.connect(self.showNextImage)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.prev_button)
        layout.addWidget(self.next_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def loadAnnotations(self):
        image_path = os.path.join(self.image_folder, self.image_files[self.current_image_index])
        self.image = cv2.imread(image_path)  # 'self.image' değişkenini burada tanımlayın

        name, _ = self.image_files[self.current_image_index].rsplit('.', 1)
        annotation_file = os.path.join(self.annotation_folder, f"{name}.txt")
        self.annotations = []  # Annotation bilgilerini sıfırlayın
        if os.path.exists(annotation_file):
            with open(annotation_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) == 5:
                        class_id, x_center, y_center, width, height = map(float, parts)

                        img_width, img_height = self.image.shape[1], self.image.shape[0]  # 'self.image' kullanın
                        x = int((x_center - width / 2) * img_width)
                        y = int((y_center - height / 2) * img_height)
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
        for annotation in self.annotations:
            x, y, w, h = annotation
            color = (0, 255, 0)  # Bounding box rengi (örneğin, yeşil)
            thickness = 2
            cv2.rectangle(self.image, (x, y), (x + w, y + h), color, thickness)

        # Görüntüyü yeniden boyutlandırın
        height, width, channel = self.image.shape
        target_width, target_height = 1280, 720  # Hedef boyutu ayarlayın
        scaled_image = cv2.resize(self.image, (target_width, target_height))

        bytes_per_line = 3 * target_width
        q_image = QImage(scaled_image.data, target_width, target_height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        self.image_label.setPixmap(pixmap)


def main():
    app = QApplication([])
    image_folder = "/home/alp/Desktop/dataset"
    annotation_folder = "/home/alp/Desktop/dataset"
    window = ObjectDetectionViewer(image_folder, annotation_folder)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
