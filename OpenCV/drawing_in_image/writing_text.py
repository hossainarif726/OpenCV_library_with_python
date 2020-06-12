import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
cv2.putText(img,'Hi Jim',(0,100),font,5,(255,0,0),5,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
