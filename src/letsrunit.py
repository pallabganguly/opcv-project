import numpy as np
import cv2

prefix = '/home/pallab/opcv-project/'
hand_cascade = cv2.CascadeClassifier(prefix + 'classifiers/' + 'cascade_20_15.xml')

img = cv2.imread(prefix + 'group.jpg')
img = cv2.resize(img, (900, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.imread(prefix + 'group.jpg', 0)

hands = hand_cascade.detectMultiScale(gray, 1.05, 9, minSize=(20, 20),maxSize=(35, 35))# minSize=(50, 50),maxSize=(80, 80))

for (x,y,w,h) in hands:
	cv2.rectangle(img,(x,y),(x+w,y+h),(200,30,200),2)

cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
