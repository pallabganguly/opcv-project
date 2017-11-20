import numpy as np
import cv2

hand_cascade = cv2.CascadeClassifier('cascade.xml')

img = cv2.imread('groupwa.jpg')
# img = cv2.resize(img, (900, 900))
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.imread('group.jpg', 0)

hands = hand_cascade.detectMultiScale(gray, 1.32, 24)
'''for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)'''
        
for (x,y,w,h) in hands:
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,31,255),2)

cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
