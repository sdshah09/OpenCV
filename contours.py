'''Contours are the borderlie of an object in an image and it is used for shape analysis,object
 detection and object recognitions'''

import numpy as np
import cv2

img = cv2.imread('orange.jpg')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thesh = cv2.threshold(imgray,127,255,0)
contours,hiearchy = cv2.findContours(thesh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
print(contours[0])

cv2.drawContours(img,contours,-1,(0,255,0),1)

cv2.imshow("image",img)
cv2.imshow('Gray Image',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()