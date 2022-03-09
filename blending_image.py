'''
Total 5 steps to be executed for blending
1. Load two images
2. Find Gaussian Pyramids of both images
3.From Gaussian Pyramids fuind their Laplacian Pyramid
4.Now join left half of one image with right half of one image
5. From this joint image pyramids reconstruct the original image
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')
print(apple.shape)
print(orange.shape)
ao = np.hstack((apple[:, :256],orange[:, 256:]))

#2. Gaussian pyramids of both
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#3. Laplacian Pyramid

apple_copy = gp_apple[5]
l_apple = [apple_copy]
for i in range(5,0,-1):
    ge = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1],ge)
    l_apple.append(laplacian)

orange_copy = gp_orange[5]
l_orange = [apple_copy]
for i in range(5,0,-1):
    ge = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1],ge)
    l_orange.append(laplacian)

#4. Add half of both images

ao_pyramid = []
n=0
for apple_lap,orange_lap in zip(l_apple,l_orange):
    n=n+1
    c,r,ch=apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(c/2)], orange_lap[:, int(c/2):]))
    ao_pyramid.append(laplacian)

#5. Reconstruct

apple_orange_reconstruct = ao_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(ao_pyramid[i], apple_orange_reconstruct)

cv2.imshow('apple',apple)
cv2.imshow('orange',orange)
cv2.imshow('apple_orange',ao)
cv2.imshow('apple_orange_blend',apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()