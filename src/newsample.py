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
	# faces = face_cascade.detectMultiScale(gray, 1.3, 8)
	hands = hand_cascade.detectMultiScale(gray, 1.03,25)
	# hands = hand_cascade.detectMultiScale(gray, 1.8,27, minSize=(25, 25), maxSize=(250, 250))
	for (x,y,w,h) in hands:
		# cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.rectangle(img,(x,y),(x+w,y+h),(79,233,252),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		# eyes = eye_cascade.detectMultiScale(roi_gray)
		hands = hand_cascade.detectMultiScale(roi_gray)
		# for (ex,ey,ew,eh) in eyes:
		# 	cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imshow('img', img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
