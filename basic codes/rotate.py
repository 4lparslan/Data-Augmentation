import cv2 

# load the input image
img = cv2.imread('test.png')

# rotate the image by 90 degree clockwise
img_cw_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# rotate the image by 270 degree clockwise or 90 degree counterclockwise
img_ccw_90 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# rotate the image by 180 degree clockwise
img_cw_180 = cv2.rotate(img, cv2.ROTATE_180)

# display the rotated image
cv2.imshow("180", img_cw_180)
cv2.imshow("cw90", img_cw_90)
cv2.imshow("ccw90", img_ccw_90)
cv2.waitKey(0)
cv2.destroyAllWindows()