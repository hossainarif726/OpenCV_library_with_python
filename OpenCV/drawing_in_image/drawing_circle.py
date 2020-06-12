import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
#cv2.circle(image,centre,width,(blue,green,red),fill)
cv2.circle(img,(200,140),100,(0,255,0),-1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
