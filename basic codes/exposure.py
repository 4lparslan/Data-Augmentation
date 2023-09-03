import numpy as np
import cv2

image = cv2.imread('test.png')
cv2.imshow("Original", image)

exposure_factor = 1.5

exposure_adjusted = np.clip(image * exposure_factor, 0, 255).astype(np.uint8)
cv2.imshow('exposure_adjusted', exposure_adjusted)

cv2.waitKey(0)
cv2.destroyAllWindows()