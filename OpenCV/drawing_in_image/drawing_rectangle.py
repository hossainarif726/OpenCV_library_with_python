import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
#cv2.rectangle(image,starting co-ord,ending co-ord,(blue,green,red),width)
cv2.rectangle(img,(15,30),(200,140),(255,0,0),5)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
