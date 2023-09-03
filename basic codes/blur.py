import cv2
import numpy as np

img = cv2.imread('test.png')

blur = cv2.blur(img,(5,5))
blur2 = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)

cv2.imshow("Original", img)

cv2.imshow("Blur", blur)
cv2.imshow("Gaussian Blur", blur2)
cv2.imshow("Median Blur", median)

cv2.waitKey(0)
cv2.destroyAllWindows()