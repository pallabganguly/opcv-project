import os
import cv2

ht = 100
i = 0
os.chdir('/home/pallab/Pictures/data')
for pic in os.listdir('.'):
    img = cv2.imread(pic, cv2.IMREAD_GRAYSCALE)
    size = 56, 100
    img = cv2.resize(img, size)
    cv2.imwrite('/home/pallab/opcv/pos/'+str(i)+'.jpg', img)
    i += 1

print('Resized', i, 'files', sep = ' ')
