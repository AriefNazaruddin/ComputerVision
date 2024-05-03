import os

import cv2

img = cv2.imread(os.path.join('C:/Users/arief/', 'Pictures', 'IMG_20190419_123827.jpg'))
img_resize = cv2.resize(img, (1024, 768))
# webcam = cv2.VideoCapture(0)

img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB)
img_hsv= cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)


# while True:
#     # ret, frame = webcam.read()
#
#     gray_webcam = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#     cv2.imshow('frame', gray_webcam)
#     if cv2.waitKey(40) & 0xFF == ord('q'):
#         break


#cv2.imshow('img_resize', img_resize)
cv2.imshow('img_rgb', img_rgb)
cv2.imshow('img_gray', img_gray)
cv2.imshow('img_hsv', img_hsv)
#webcam.release()
#cv2.destroyAllWindows()
cv2.waitKey(0)
