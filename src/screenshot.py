

import cv2
import os
cam = cv2.VideoCapture(0)


name=input("donner le nom :")
counter=1
while True:
    ret, frame = cam.read()
    
    cv2.imshow("Webcam Screenshot",frame)
    
    k=cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if k%256 == 32:
        img_name ="face/data/{}_{}.png".format(name,counter)
        cv2.imwrite(img_name,frame)
        counter+=1


        
cam.release()
cv2.destroyAllWindows ()