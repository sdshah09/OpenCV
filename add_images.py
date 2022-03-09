import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img1 = cv2.imread('opencv-logo.png')

img = cv2.resize(img,(512,512))
img1 = cv2.resize(img1,(512,512))

#dst = cv2.add(img,img1)
dst = cv2.addWeighted(img,.9,img1,.1,0)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()