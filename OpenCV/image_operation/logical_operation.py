import cv2
import numpy as np

#loading images
img1 = cv2.imread('test1.png')
img2 = cv2.imread('test3.png')

#defining region of img1 with size of img2
rows, cols, channels = img2.shape
roi = img1[0:rows,0:cols]

#converting to grayscale and masking it for transparen background
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

#applying mask to the img1
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('Final',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
