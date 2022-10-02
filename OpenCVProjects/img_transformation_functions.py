import cv2
import numpy as np

img = cv2.imread('images/OpenCV.jpg')

new_img = np.zeros(img.shape, dtype = 'uint8')

#img = cv2.flip(img, 1) # mirroring
# -1 по вертикали и по горизонтали
# 0 по вертикали  
# 1 по горизонтали

def rotate(img_param, angle):
	height, width = img_param.shape[:2]
	point = (width//2, height//2) 

	mat = cv2.getRotationMatrix2D(point, angle, 1) # zoom scale
	return cv2.warpAffine(img_param, mat, (width, height))


def transform(img_param, x, y):
	height, width = img_param.shape[:2]
	mat = np.float32([[1, 0, x], [0, 1, y]])
	return cv2.warpAffine(img_param, mat, (width, height))

#img = rotate(img, 90)
#img = transform(img, 30, 200)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5,5), 0)

img = cv2.Canny(img, 100, 140) # all colors [0;99] => 0 and [141;255] => 1

# contours and object hierarchy 
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) 

cv2.drawContours(new_img, con, -1, (230, 111, 48), 1) # using contours previous img
# -1 contour id
# 1 thickness

cv2.imshow("Result", new_img)
cv2.waitKey(0)