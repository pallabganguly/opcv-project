import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

hand_cascade = cv2.CascadeClassifier('cascade_30_15.xml')
neighbours = [1, 3, 5, 10, 15, 20, 30, 40, 50]
acc = []
count = 0

for n in neighbours:
	for pic in os.listdir('/home/pallab/opcv/test30'):
		fn = pic[:-4]
		pp = fn.split('_')
		vals = list(map(int,pp))
		img = cv2.imread(pic)
		gray = cv2.imread(pic, 0)
		hands = hand_cascade.detectMultiScale(gray, 1.03, n)
		for (x,y,w,h) in hands:
			print((x,y,w,h))
			if abs(vals[1]-x)/vals[1] < 0.8 and abs(vals[2]-y)/vals[2] < 0.8:
				count += 1
				print('huha')
			elif abs(vals[3]*vals[4] - w*h) / (vals[3]*vals[4]) < 0.8:
				count += 1
				print('huha')
	acc.append(count)
	count = 0
print(acc)
plt.plot(neighbours, acc)
plt.show()