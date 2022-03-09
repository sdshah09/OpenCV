''' when we click on any point of that image it will pop a new window
showing that color in that new window'''

import numpy as np
import cv2

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        mycolorimage = np.zeros((512,512,3),np.uint8)
        mycolorimage[:]=[blue,green,red]
        cv2.imshow('color',mycolorimage)
img = cv2.imread('lena.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()