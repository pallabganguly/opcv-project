import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
ssize = len(os.listdir('test30'))
acc = []
hand_cascade = cv2.CascadeClassifier('cascade_50_15.xml')
values = [5, 10, 15, 20, 50, 75, 100, 125, 150]
zoom = [1.01, 1.03, 1.05, 1.10, 1.15, 1.20, 1.25, 1.35, 1.50]
for n in values:
	count = 0
	for path in os.listdir('test30'):
		img = cv2.imread('test30/'+path)
		gray = cv2.imread('test30/'+path, 0)
		hands = hand_cascade.detectMultiScale(gray, 1.03, n)
		for (x,y,w,h) in hands:
			fn = path[:-4]
			pp = fn.split('_')
			vals = list(map(int,pp))
			us, xd, yd, wd, hd = vals
			if abs(xd-x)/xd < 0.8 or abs(yd-y)/yd < 0.8:
				count += 1
	count = min(count, ssize)
	acc.append((count/ssize)*100)
	print("n =",n, "Accuracy:",(count/ssize))
plt.plot(values, acc)
plt.xlabel('No. of neighbours')
plt.ylabel('Accuracy %')
plt.show()
# cv2.imshow('result',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
