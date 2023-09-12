import numpy as np
import cv2 as cv

img = cv.imread('test.png', 0)
rows, cols = img.shape

cv.imshow("Original", img)

# X Axis
M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
sheared_img = cv.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))
cv.imshow('sheared_x-axis', sheared_img)

# Y Axis
M = np.float32([[1,   0, 0], [0.5, 1, 0], [0,   0, 1]])
sheared_img = cv.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))
cv.imshow('sheared_y-axis', sheared_img)

cv.waitKey(0)
cv.destroyAllWindows()