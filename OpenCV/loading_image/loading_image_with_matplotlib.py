import cv2
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(img, cmap='gray',interpolation = 'bicubic')
#there will be a change of color because color order of OpenCV is BGR
#and we are feeding BGR to a RGB color order
plt.show()
