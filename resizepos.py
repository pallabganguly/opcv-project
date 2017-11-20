import os
import cv2

ht = 50
i = 0
os.chdir('/home/pallab/Desktop/files')
for pic in os.listdir('.'):
    img = cv2.imread(pic, cv2.IMREAD_GRAYSCALE)
    size = ht, ht
    img = cv2.resize(img, size)
    cv2.imwrite('/home/pallab/opcv/pos'+str(ht)+'/p'+str(i)+'.jpg', img)
    i += 1

print('Resized', i, 'files', sep = ' ')
