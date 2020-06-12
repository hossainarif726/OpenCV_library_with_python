import cv2
import numpy as np

img1 = cv2.imread('test1.png')
img2 = cv2.imread('test2.png')

#for adding two image must be in same shape
weighted = cv2.addWeighted(img1,0.4,img2,0.6,0)
cv2.imshow('weighted add image',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
