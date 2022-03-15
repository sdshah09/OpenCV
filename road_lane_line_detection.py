import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('road.jpeg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

print(img.shape)
height = img.shape[0] # [0] for 1st index of height of image
width = img.shape[1] #[1] for 2nd index of width of image road

roi_vertices = [
    (20,473),(516,300),(995,485)
]

def roi(image,vertices):
    mask = np.zeros_like(image)
    channel_count = image.shape[2]
    match_mask_color = (255,)*channel_count
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_img = cv2.bitwise_and(image,mask)
    return masked_img

cropped_image = roi(img,np.array([roi_vertices],np.int32))
plt.imshow(img)
plt.imshow(cropped_image)
plt.show()
#cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()