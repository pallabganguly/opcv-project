import os
import cv2

ht = 100
i = 0
os.chdir('/home/pallab/opcv/pos')
for pic in os.listdir('.'):
    img = cv2.imread(pic, cv2.IMREAD_GRAYSCALE)
    #img = cv2.resize(img, (ht, ht))
    cv2.imwrite('/home/pallab/opcv/pos/'+str(i)+'.jpg', img)
    i += 1

print('Resized and greyed', i, 'files', sep = ' ')
