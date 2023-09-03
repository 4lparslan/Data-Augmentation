import cv2
import numpy as np

image = cv2.imread('test.png')

hue_shift = 12 # 0-179

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv_image[:,:,0] = np.clip(hsv_image[:,:,0] + hue_shift, 0, 255) % 180

output_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

cv2.imshow("Original", image)
cv2.imshow("Hue", output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()