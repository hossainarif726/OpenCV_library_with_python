import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
pts = np.array([[10,5],[20,30],[70,80],[100,150]],np.int32)
#cv2.polylines(image, [pts], isClosed, color, thickness)
cv2.polylines(img,[pts],True,(0,255,0),5)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
