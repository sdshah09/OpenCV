## to draw geometric shapes on the image made using numpy
import numpy as np
import cv2
img = np.zeros([512,512,3],np.uint8)
                #point1    #point2   #bgr   #thickness
img = cv2.line(img,(0,0),(480,480),(210,118,222),5)
img = cv2.arrowedLine(img,(0,300),(300,300),(210,118,222),5)
                    #vertex1  #vertex2
img=cv2.rectangle(img,(384,0),(510,128),(0,0,300),5)
            #centre point #radius
img=cv2.circle(img,(0,255),45,(0,300,0),-1)


pts = np.array([[100,200], [25,20], [300,400]])
print(pts)
img=cv2.polylines(img,[pts],True,(255,255,255),5)
img = cv2.ellipse(img,(200,400),(100,50),0,0,360,(255,255,255),5)
font = cv2.FONT_HERSHEY_PLAIN
img=cv2.putText(img,"Shaswat",(10,500),font,4,(255,255,255),5,cv2.LINE_8)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()