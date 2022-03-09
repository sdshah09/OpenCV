'''Laplacian pyramid is formed by the difference between that levell
in Gaussian Pyramid and expanded versons of its upper level in Gaussian Pyramid '''

import cv2
import numpy as np
img = cv2.imread('lena.jpg')
layer = img.copy()
g = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    g.append(layer)
    #cv2.imshow(str(i),layer)
layer = g[5]
cv2.imshow('upper level gaussian pyramid',layer)
l = [layer]

for i in range(5,0,-1):
    ge = cv2.pyrUp(g[i])
    laplacian = cv2.subtract(g[i-1],ge) #gaussian pyramid - gaussian extended upper version = laplacian
    cv2.imshow(str(i),laplacian)
cv2.imshow('og',img)
cv2.waitKey(0)
cv2.destroyAllWindows()