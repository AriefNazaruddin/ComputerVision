import os
import cv2

img = cv2.imread(os.path.join('.', 'Data', 'handwritten.png'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

Adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

ret, simple_thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('Adaptive thresh', Adaptive_thresh)
cv2.imshow('Simple thresh', simple_thresh)
cv2.waitKey(0)