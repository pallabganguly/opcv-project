import numpy as np
import cv2

hand_cascade = cv2.CascadeClassifier('cascade_50_10.xml')

img = cv2.imread('dec17.jpg')
# img = cv2.resize(img, (900, 900))
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.imread('dec17.jpg', 0)

hands = hand_cascade.detectMultiScale(gray, 1.95, 12, minSize=(60,60))

for (x,y,w,h) in hands:
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,30,255),2)

cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
