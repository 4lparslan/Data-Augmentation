import cv2

# Annotation değerleri
class_id, x_center, y_center, width, height = 0, 0.7009479166666667, 0.5648240740740741, 0.06257161458333348, 0.11132407407407409

# İmajı yükleyin (örnek olarak, imajın yolu)
image_path = "/home/alp/Desktop/dataset/2.jpg"
image = cv2.imread(image_path)

# İmajın genişlik ve yüksekliğini alın
img_height, img_width, _ = image.shape

# Bbox koordinatlarını hesaplayın
x = int(x_center * img_width)
y = int(y_center * img_height)
w = int(width * img_width)
h = int(height * img_height)

# Bbox'ı çizin (örneğin, yeşil)
color = (0, 255, 0)
thickness = 2
cv2.rectangle(image, (x - w // 2, y - h // 2), (x + w // 2, y + h // 2), color, thickness)

# İmajı görüntüleyin
cv2.imshow("Image with Bbox", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
