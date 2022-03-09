## to draw geometric shapes on the image
import numpy as np
import cv2
img = cv2.imread('lena.jpg',1)
                #point1    #point2   #bgr   #thickness
img = cv2.line(img,(0,0),(480,480),(210,118,222),5)
img = cv2.arrowedLine(img,(0,300),(300,300),(210,118,222),5)
                    #vertex1  #vertex2
img=cv2.rectangle(img,(384,0),(510,128),(0,0,300),5)
            #centre point #radius
img=cv2.circle(img,(0,255),45,(0,300,0),-1)
font = cv2.FONT_HERSHEY_PLAIN
img=cv2.putText(img,"Shaswat",(10,500),font,4,(255,255,255),5,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()