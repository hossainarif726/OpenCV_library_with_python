import cv2
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('saved image.png',img)
