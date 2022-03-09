#Gaussian pyramid is use to create small or big images
# and are usefel in blending or reconstruction of images

import cv2
import numpy as np
img = cv2.imread('lena.jpg')
layer = img.copy()
g = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    g.append(layer)
    cv2.imshow(str(i),layer)
cv2.waitKey(0)
cv2.destroyAllWindows()