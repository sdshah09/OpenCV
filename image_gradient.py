# An image gradient is a directional change in the intensity or color in an image

import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    print(x)
cv2.namedWindow('image')
cv2.createTrackbar('gradience and edge','image',10,500,nothing)
img = cv2.imread('messi5.jpg',0)
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap)) # to convert float negative image into int absolute image
sobelX = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
 
sobelCombined = cv2.bitwise_or(sobelX,sobelY)
canny = cv2.Canny(img,100,200)
titles = ['image','Laplacian','sobelX','sobelY','Sobel combine','canny']
images = [img,lap,sobelX,sobelY,sobelCombined,canny]

for i in range(6):
    plt.subplot(3,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()

while(1):
    cv2.getTrackbarPos('gradience and edge','image')


