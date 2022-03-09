# Histograms is a graph or plot which gives overall intensity of the image
# X axis intensity range upto 256
# Y axis pixel*pixel range

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.zeros((200,200),np.uint8);
cv2.rectangle(img,(0,100),(200,200),(255),-1)
cv2.rectangle(img,(0,50),(100,100),(127),-1)

img1 = cv2.imread("lena.jpg")
b, g, r = cv2.split(img1)
cv2.imshow("img1", img1)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)

plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

cv2.imshow("img",img)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()