# in this program we get to know abut how to fin
# the shape size and datatype of the image
# ROI(region of interest)=copy an onject on another place in the same image
import cv2
import numpy as np

img = cv2.imread('messi5.jpg')

print(img.shape) #returns a tuple number of rows coloumns and channels
print(img.size) #returns total numbers of pixel is accessed
print(img.dtype) #return image datatype
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340,330:390]
img[273:333,100:160] = ball

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()