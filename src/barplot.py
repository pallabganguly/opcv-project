import numpy as np
import cv2
import os
# from matplotlib import pyplot as plt
from bokeh.plotting import figure, show, output_file

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
output_file('vbar.html')

prefix = '/home/pallab/opcv-project/'
ssize = len(os.listdir(prefix+'test50'))
classifiers = ['cascade_20_20.xml', 'cascade_25_20.xml']#, 'cascade_40x40.xml', 'cascade_50_10.xml', 'cascade_50_15.xml']
acc = []
for classifier in classifiers:
	count = 0
	for path in os.listdir(prefix+'test50'):
		img = cv2.imread(prefix+'test50/'+path)
		gray = cv2.imread(prefix+'test50/'+path, 0)
		hand_cascade = cv2.CascadeClassifier(prefix+'classifiers/'+classifier)
		hands = hand_cascade.detectMultiScale(gray, 1.03, 5)
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

# creating plot

p = figure(plot_width=400, plot_height=400)
p.hbar(y=[1, 2], height=0.5, left=0,
       right=acc, color="gray")

show(p)
