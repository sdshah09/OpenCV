#Morphological transformations are some simple operations based on the
# image shape. It is normally performed on binary images. It needs two inputs, one is
# our original image, second one is called structuring element or kernel which decides the nature of operation.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernel = np.zeros((5,5),np.uint8)
dilation = cv2.dilate(mask, kernel, iterations=2)
erosion = cv2.erode(mask, kernel, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) #opening = erosion then dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) #closing = dilation then erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
th1 = cv2.morphologyEx(mask,cv2.MORPH_RECT,kernel)
th2= cv2.morphologyEx(mask,cv2.MORPH_ELLIPSE,kernel)
titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th','th1','th2']
images = [img, mask, dilation, erosion, opening, closing, mg, th,th1,th2]

for i in range(10):
    plt.subplot(2, 5, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()