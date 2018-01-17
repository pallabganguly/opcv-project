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

# data to plot
prefix = '/home/pallab/opcv-project/'
ssize = len(os.listdir(prefix+'test50'))
classifiers = ['cascade_20_15.xml', 'cascade_30x30.xml', 'cascade_40x40.xml', 'cascade_50_10.xml', 'cascade_50_15.xml']
acc = []
for classifier in classifiers:
	count = 0
	for path in os.listdir(prefix+'test50'):
		img = cv2.imread(prefix+'test50/'+path)
		gray = cv2.imread(prefix+'test50/'+path, 0)
		hand_cascade = cv2.CascadeClassifier(prefix+'classifiers/'+classifier)
		hands = hand_cascade.detectMultiScale(gray, 1.99, 5)
		for (x,y,w,h) in hands: # (x, y, w, h) predicted values
			fn = path[:-4]
			pp = fn.split('_')
			vals = list(map(int,pp))
			us, xd, yd, wd, hd = vals # (xd, yd, wd, hd) actual values
			iarea = intersectingArea(x, y, x+w, y+h, xd, yd, xd+wd, yd+hd)
			if abs(iarea)/abs(wd*hd) >= 0.75:
				count += 1

	acc.append((count/ssize)*100)
	print(classifier, 'Accuracy:',(count/ssize)*100)

n_groups = 5
 
# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(classifiers, acc, bar_width,
                 alpha=opacity,
                 color='c',
                 )
 
 
plt.xlabel('Classifier')
plt.ylabel('Accuracy %')
plt.title('Accuracy with different classifiers')
plt.xticks(index + bar_width, ('20x20', '30x30', '40x40', '50x50,10', '50x50,15'))
plt.legend()
 
plt.tight_layout()
plt.show()