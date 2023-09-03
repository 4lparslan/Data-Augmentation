import cv2
import numpy as np

# Load the image
img = cv2.imread('test.png')

# Generate random Gaussian noise
mean = 0
stddev = 180
noise = np.zeros(img.shape, np.uint8)
cv2.randn(noise, mean, stddev)

# Add noise to image
noisy_img = cv2.add(img, noise)

cv2.imshow("Original", img)
cv2.imshow("Noise", noisy_img)
cv2.waitKey(0)

cv2.destroyAllWindows()