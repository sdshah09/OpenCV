import cv2
img=cv2.imread('lena.jpg',-1) #read the image
print(img)
cv2.imshow("image",img) #show the image

k=cv2.waitKey(0) #increase the time for to image to stay open

#27 is escape key number and we want to destoy only when escape key is pressed
if k==27:
    cv2.destroyAllWindows()
elif k == ord('s'): #pressing s it will save the image in another copy``
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()