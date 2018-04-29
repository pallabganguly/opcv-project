import numpy as np
import cv2

#face_cascade = cv2.CascadeClassifier('casc.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
prefix = '/home/pallab/opcv-project/classifiers/'
hand_cascade = cv2.CascadeClassifier(prefix+'cascade_20_15.xml')

cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	hands = hand_cascade.detectMultiScale(gray, 1.05, 7, minSize=(50, 50),maxSize=(80, 80))
	for (x, y, w, h) in hands:
		cv2.rectangle(img,(x,y),(x+w,y+h),(79,233,252),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = roi_color = img[y:y+h, x:x+w]

	cv2.imshow('img', img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
