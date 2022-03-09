import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(i):
    pass

cv2.namedWindow("image")
cv2.createTrackbar('x',"image",0,100,nothing)
cv2.createTrackbar('y',"image",0,100,nothing)
while(1):
    img = cv2.imread('lena.jpg',0)
    x=cv2.getTrackbarPos('x',"image")
    y=cv2.getTrackbarPos('y',"image")
    canny= cv2.Canny(img,x,y)

cv2.imshow("image",img)
cv2.imshow("image",canny)
k=cv2.waitKey(0)
if k == 27:
    exit()

cv2.destroyAllWindows()