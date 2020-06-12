import cv2
import numpy as np

img1 = cv2.imread('test1.png')
img2 = cv2.imread('test2.png')

#for adding two image must be in same shape
add = cv2.add(img1,img2) #it will destroy opaqueness
cv2.imshow('added image',add)
cv2.waitKey(0)
cv2.destroyAllWindows()
