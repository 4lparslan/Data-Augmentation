import cv2

img = cv2.imread('test.png')

# flip the image by vertically
img_v = cv2.flip(img, 0)

# flip the image by horizontally
img_h = cv2.flip(img, 1)

# display the rotated image
cv2.imshow("Original", img)
cv2.imshow("Vertical Flip", img_v)
cv2.imshow("Horizontal Flip", img_h)
cv2.waitKey(0)
cv2.destroyAllWindows()