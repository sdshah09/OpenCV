''' to create a code for object detection  using hsv(hue saturation value)
which will give only blue balls if asked about blue through mask
 using trackbar '''

import numpy as np
import cv2 as cv

def nothing(x):
    pass

cap = cv.VideoCapture(0)
cv.namedWindow('Tracking')
cv.createTrackbar('LH','Tracking',0,255,nothing)
cv.createTrackbar('LS','Tracking',0,255,nothing)
cv.createTrackbar('LV','Tracking',0,255,nothing)
cv.createTrackbar('HH','Tracking',255,255,nothing)
cv.createTrackbar('HS','Tracking',255,255,nothing)
cv.createTrackbar('HV','Tracking',255,255,nothing)
while True:
    #frame = cv.imread('smarties.png')
    _, frame = cap.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lh = cv.getTrackbarPos('LH','Tracking')
    ls = cv.getTrackbarPos('LS', 'Tracking')
    lv = cv.getTrackbarPos('LV', 'Tracking')

    uh = cv.getTrackbarPos('HH', 'Tracking')
    us = cv.getTrackbarPos('HS', 'Tracking')
    uv = cv.getTrackbarPos('HV', 'Tracking')

    lb = np.array([ls,lh,lv]) # lower boundary
    ub = np.array([uh,us,uv]) # upper boundary

    mask = cv.inRange(hsv,lb,ub)
    result = cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('result',result)

    k = cv.waitKey(1)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()