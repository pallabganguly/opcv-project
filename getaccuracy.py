import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

ssize = len(os.listdir('test50'))
acc = []
values = [5, 10, 15, 20, 50, 75, 100, 125, 150]
zoom = [1.01, 1.03, 1.05, 1.10, 1.15, 1.20, 1.25, 1.35, 1.50]
cscd = ['cascade_20x20.xml','cascade_30x30.xml', 'cascade_40x40.xml', 'cascade_50x50.xml']
hand_cascade = cv2.CascadeClassifier('cascade_50_10.xml')

for n in values:
	count = 0
	for path in os.listdir('test50'):
		img = cv2.imread('test50/'+path)
		gray = cv2.imread('test50/'+path, 0)
		hands = hand_cascade.detectMultiScale(gray, 1.03, n)
		for (x,y,w,h) in hands:
			fn = path[:-4]
			pp = fn.split('_')
			vals = list(map(int,pp))
			us, xd, yd, wd, hd = vals
			if abs(xd-x)/xd < 0.8 and abs(yd-y)/yd < 0.8:
				count += 1
	count = min(count, ssize)
	acc.append((count/ssize)*100)
	print('n: ', n, 'Accuracy:',(count/ssize))
plt.plot(values, acc)
plt.xlabel('Neighbours')
plt.ylabel('Accuracy %')
plt.show()