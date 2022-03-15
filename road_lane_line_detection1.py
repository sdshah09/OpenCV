import cv2
import numpy as np
from matplotlib import pyplot as plt


def roi(img, vertices):
    mask = np.zeros_like(img)

    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img

def draw_lines(img,lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blank_image, (x1,y1) , (x2,y2) , (0,255,0) , thickness=2)

    img = cv2.addWeighted(image,0.8,blank_image,1,0.0)
    return img

image = cv2.imread('road.jpeg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0] # [0] for 1st index of height of image
width = image.shape[1] #[1] for 2nd index of width of image road

roi_vertices = [
    (20,473),(512,296),(995,485)
]
#(516,300),

'''For Bitwise_and you need to know the following two rules

Black + Any Color = Black
White + Any Color = That Color'''

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

canny_image = cv2.Canny(gray_image,100,200)
#cv2.imshow('canny',canny_image)
cropped_image = roi(canny_image,np.array([roi_vertices],np.int32))

lines = cv2.HoughLinesP(cropped_image,
                        rho=1,
                        theta=np.pi/180,  #To get sine value of the angle in radians, need to multiply angle with np.pi/180.

                        threshold=100,
                        lines=np.array([]),
                        minLineLength=200,
                        maxLineGap=10)

image_with_lines = draw_lines(image,lines)
plt.imshow(image_with_lines)
# plt.imshow(img)
# plt.imshow(cropped_image)
plt.show()
#cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()