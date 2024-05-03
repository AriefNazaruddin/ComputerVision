# crop

import os
import cv2

img = cv2.imread(os.path.join('.', 'Data', 'racoon.jpg'))

print(img.shape)

cropped_img = img[120:840, 320:940]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)