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
ssize = len(os.listdir(prefix+'test50'))
acc = []
values = [x for x in range(2, 100)]
zoom = [1.01+x*0.01 for x in range(0, 100)]
thres = [0.45+0.02*x for x in range(0, 15)]
hand_cascade = cv2.CascadeClassifier(prefix+'classifiers/cascade_40x40.xml')

for n in thres:
	count = 0
	for path in os.listdir(prefix+'test50'):
		img = cv2.imread(prefix+'test50/'+path, 0)
		# print(hand_cascade.load(prefix+'classifiers/cascade_40x40.xml'))
		hands = hand_cascade.detectMultiScale(img, 1.03, 5)
		for (x,y,w,h) in hands: # (x, y, w, h) predicted values
			fn = path[:-4]
			pp = fn.split('_')
			vals = list(map(int,pp))
			us, xd, yd, wd, hd = vals # (xd, yd, wd, hd) actual values
			iarea = intersectingArea(x, y, x+w, y+h, xd, yd, xd+wd, yd+hd)
			if abs(iarea)/abs(wd*hd) >= n:
				count += 1
	# count = min(count, ssize)
	# acc.append((count/ssize)*100)
	# print('n:', n, 'Accuracy:',(count/ssize))
	acc.append(count)
	print('n:',n, 'Acc:',count)
plt.plot(thres, acc)
# plt.text(4, 8, 'Neigh=5, Scale=1.03', style='italic')
plt.title('Count of positives vs Threshold')
plt.xlabel('Threshold')
plt.ylabel('Counts (Actual=200)')
plt.show()
