import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

def intersectingArea(a ,b ,c ,d ,e ,f ,g ,h):
    if e>=c or a >= g or b >= h or f>=d:
        return 0

    topleftx = max(a ,e)
    toplefty = max(b ,f)
    bottomrightx = min(c ,g)
    bottomrighty = min(d ,h)
    area = (bottomrightx - topleftx) * (bottomrighty - toplefty)
    return area

prefix = '/home/pallab/opcv-project/'
ssize = len(os.listdir(prefix+'small-test'))
print('Test-set size: ', ssize)
acc = []
# zoom = [1.01+x*0.01 for x in range(0, 100)]
zoom = [1.02+x*0.01 for x in range(0, 120)]
hand_cascade = cv2.CascadeClassifier(prefix+'classifiers/cascade_20_15.xml')
print('Cascade Loaded: ', hand_cascade.load(prefix+'classifiers/cascade_20_15.xml'))

for n in zoom:
	count = 0
	for path in os.listdir(prefix+'small-test'):
		img = cv2.imread(prefix+'small-test/'+path, 0)
		hands = hand_cascade.detectMultiScale(img, n, 5)
		for (x,y,w,h) in hands: # (x, y, w, h) predicted values
			fn = path[:-4]
			pp = fn.split('_')
			vals = list(map(int,pp))
			us, xd, yd, wd, hd = vals # (xd, yd, wd, hd) actual values
			iarea = intersectingArea(x, y, x+w, y+h, xd, yd, xd+wd, yd+hd)
			if abs(iarea)/abs(wd*hd) >= 0.70:
				count += 1
	# count = min(count, ssize)
	acc.append((count/ssize)*100)
	print('n:', n, 'Accuracy:',(count/ssize))
	# acc.append(count)
	# print('n:',n, 'Acc:',count)

plt.plot(zoom, acc)
acc = []

hand_cascade = cv2.CascadeClassifier(prefix+'classifiers/cascade_30_15.xml')
print('Cascade Loaded: ', hand_cascade.load(prefix+'classifiers/cascade_30_15.xml'))
for n in zoom:
	count = 0
	for path in os.listdir(prefix+'small-test'):
		img = cv2.imread(prefix+'small-test/'+path, 0)
		hands = hand_cascade.detectMultiScale(img, n, 2)
		for (x,y,w,h) in hands: # (x, y, w, h) predicted values
			fn = path[:-4]
			pp = fn.split('_')
			vals = list(map(int,pp))
			us, xd, yd, wd, hd = vals # (xd, yd, wd, hd) actual values
			iarea = intersectingArea(x, y, x+w, y+h, xd, yd, xd+wd, yd+hd)
			if abs(iarea)/abs(wd*hd) >= 0.70:
				count += 1
	# count = min(count, ssize)
	acc.append((count/ssize)*100)
	print('n:', n, 'Accuracy:',(count/ssize))

plt.plot(zoom, acc)
# plt.text(4, 8, 'Neigh=3, Thres=0.70', style='italic')
plt.title('Accuracy vs Scale Factor')
plt.xlabel('Scale Factor')
plt.ylabel('Accuracy %')
plt.legend(['WindowSize=20', 'WindowSize=30'], loc='upper right')
plt.show()
