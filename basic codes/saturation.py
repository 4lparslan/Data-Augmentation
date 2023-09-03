import cv2
import numpy as np

image = cv2.imread('test.png')

saturation_factor = 1.5

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hsv_image[:,:,1] = np.clip(hsv_image[:,:,1] * saturation_factor, 0, 255).astype(np.uint8)

output_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

cv2.imshow("Original", image)
cv2.imshow("Saturation", output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()