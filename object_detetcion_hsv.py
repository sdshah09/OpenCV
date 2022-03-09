''' to create a code for object detection  using hsv(hue saturation value)
which will give only blue balls if asked about blue through mask   '''
import cv2
import numpy as np
import cv2 as cv

def nothing(x):
    pass

while True:
    frame = cv.imread('smarties.png')
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    lb = np.array([110,50,50]) # lower boundary of blue color array
    ub = np.array([130,255,255]) # upper boundary of blue color array
    mask = cv.inRange(hsv,lb,ub)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('result',result)

    k = cv.waitKey(1)
    if k == 27:
        break
