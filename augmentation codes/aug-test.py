from augmentations import *

img = cv2.imread("test.png")


####SENSITIVE-ROTATE TEST####
#Send 0-45 degree angle
rotated = SensitiveRotate(img, 45, [[249,256,289,276],[316,256,348,278]])
rot_img, rot_annots = rotated.ApplySensitiveRotate()

for bbox in rot_annots:
	cv2.rectangle(rot_img, (bbox[0],bbox[1]), (bbox[2],bbox[3]), (0, 255, 0), thickness=2)
cv2.imshow("rotated", rot_img)

cv2.waitKey(0)
cv2.destroyAllWindows()




####ROTATE TEST####
#Send 90, 180 or 270 degree angle
# rotated = rotate.Rotate(img, 180, [[249,256,289,276],[316,256,348,278]])
# rot_img, rot_annots = rotated.ApplyRotate()

# for bbox in rot_annots:
# 	cv2.rectangle(rot_img, (bbox[0],bbox[1]), (bbox[2],bbox[3]), (0, 255, 0), thickness=2)
# cv2.imshow("rotated", rot_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()




####BRIGHTNESS TEST####
# b = brightness.Brightness(75, img)
# bright_img = b.ApplyBrightness()

# cv2.imshow("brightness", bright_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




####SATURATION TEST####
# saturated = saturation.Saturation(80, img)
# saturated_img = saturated.ApplySaturation()

# cv2.imshow("saturated", saturated_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




####HUE TEST####
# hued = hue.Hue(10, img)
# hue_img = hued.ApplyHue()

# cv2.imshow("noised", hue_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



####NOISE TEST####
# noised = noise.Noise(3, img)
# noised_img = noised.ApplyNoise()

# cv2.imshow("noised", noised_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



####FLIP TEST####
# flipped = flip.Flip(img, False, True, [[249,256,289,276],[316,256,348,278]])
# flip_img, flip_annots = flipped.ApplyFlip()

# for bbox in flip_annots:
# 	cv2.rectangle(flip_img, (bbox[0],bbox[1]), (bbox[2],bbox[3]), (0, 255, 0), thickness=2)
# cv2.imshow("flipped", flip_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()



####BLUR TEST####
# blurred = blur.Blur(1, img)
# blurred_img = blurred.ApplyBlur()

# cv2.imshow("blurred", blurred_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

