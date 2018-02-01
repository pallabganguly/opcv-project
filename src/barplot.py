import numpy as np
import cv2
import os
from matplotlib import pyplot as plt
# from bokeh.plotting import figure, show, output_file

def intersectingArea(a ,b ,c ,d ,e ,f ,g ,h):
    if e>=c or a >= g or b >= h or f>=d:
        return 0

    topleftx = max(a ,e)
    toplefty = max(b ,f)
    bottomrightx = min(c ,g)
    bottomrighty = min(d ,h)
    area = (bottomrightx - topleftx) * (bottomrighty - toplefty)
    return area

# output file for bokeh bar chart
# output_file('vbar.html')

prefix = '/home/pallab/opcv-project/'
ssize = len(os.listdir(prefix+'small-test'))
classifiers = ['cascade_20_15.xml', 'cascade_30_15.xml', 'cascade_40x40.xml', 'cascade_50_15.xml']
label = ['20px', '30px', '40px', '50px']
acc = []
for classifier in classifiers:
	count = 0
	for path in os.listdir(prefix+'small-test'):
		img = cv2.imread(prefix+'small-test/'+path)
		gray = cv2.imread(prefix+'small-test/'+path, 0)
		hand_cascade = cv2.CascadeClassifier(prefix+'classifiers/'+classifier)
		hands = hand_cascade.detectMultiScale(gray, 1.05, 6) # 1.08, 6
		for (x,y,w,h) in hands: # (x, y, w, h) predicted values
			fn = path[:-4]
			pp = fn.split('_')
			vals = list(map(int,pp))
			us, xd, yd, wd, hd = vals # (xd, yd, wd, hd) actual values
			iarea = intersectingArea(x, y, x+w, y+h, xd, yd, xd+wd, yd+hd)
			if abs(iarea)/abs(wd*hd) >= 0.70:
				count += 1

	acc.append(count)
	print(classifier, 'Hits:',count)

# creating plot
indices = np.arange(len(classifiers)) # generate indices 1 through 5
plt.barh(indices, acc)
plt.xlabel('No. of positives')
plt.ylabel('Classifier Window Size')
plt.yticks(indices, label, rotation=30)
plt.title('Positives detected by classifier')
plt.show()
