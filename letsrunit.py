import numpy as np
import cv2

hand_cascade = cv2.CascadeClassifier('cascade.xml')

img = cv2.imread('groupwa.jpg')
# img = cv2.resize(img, (900, 900))
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.imread('group.jpg', 0)

hands = hand_cascade.detectMultiScale(gray, 1.32, 24)

for (x,y,w,h) in hands:
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,31,255),2)

cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
