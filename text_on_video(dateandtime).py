import cv2
import datetime

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc("X","V","I","D")
#https://www.fourcc.org/fourcc.php (to understand fourcc)
out = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))
#second argument i.e. 20 is frames per second
print(cap.isOpened())
while(cap.isOpened()):
     ret,frame = cap.read() #ret = boolean varialble
                              #frame
     #to convert into grayscale use cvtColor function
     #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     if ret == True:
         out.write(frame)
         txt = "Height: " + str(cap.get(3)) + " Width: " + str(cap.get(4))
         date = str(datetime.datetime.now())
         font = cv2.FONT_HERSHEY_PLAIN
         frame=cv2.putText(frame,date,(10,50),font,1,(255,255,255),1,cv2.LINE_AA)
         cv2.imshow('frame',frame)

         if cv2.waitKey(1) & 0xFF == ord('q'):
             break
     else:
        break
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
'''cap.set(3,1280)
cap.set(4,720)
print(cap.get(3))
print(cap.get(4))'''

cap.release()
out.release()
cv2.destroyAllWindows()
