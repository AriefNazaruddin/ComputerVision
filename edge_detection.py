import os
import cv2
import numpy as np

img = cv2.imread(os.path .join('.', 'Data', 'basketball-player.jpg'))

img_edge = cv2.Canny(img, 120, 125)

img_edge_d= cv2.dilate(img_edge, np.ones((3,3), dtype=np.int8))

img_edge_e = cv2.erode(img_edge_d, np.ones((3,3), dtype=np.int8))

cv2.imshow('img', img)
cv2.imshow('edge', img_edge)
cv2.imshow('edge_d', img_edge_d)
cv2.imshow('edge_e', img_edge_e)
cv2.waitKey(0)





# img_ori = cv2.imread(os.path .join('C:/Users/arief/','Downloads',  'IMG_0094.jpeg'))
#
# webcam = cv2.VideoCapture(0)
#
# img = cv2.resize(img_ori, (364, 273))
#
# #img_edge = cv2.Canny(img, 120, 125)
#
# #img_edge_d= cv2.dilate(img_edge, np.ones((3,3), dtype=np.int8))
#
# #img_edge_e = cv2.erode(img_edge_d, np.ones((3,3), dtype=np.int8))
#
# while True:
#     ret, frame = webcam.read()
#
#     #img_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2LUV)
#     img_edge = cv2.Canny(frame, 120, 125)
#     img_edge_d = cv2.dilate(img_edge, np.ones((3, 3), dtype=np.int8))
#     img_edge_e = cv2.erode(img_edge_d, np.ones((3, 3), dtype=np.int8))
#
#     cv2.imshow('frame',  img_edge_e)
#     if cv2.waitKey(40) & 0xFF == ord('q'):
#         break
#
#
#
# #cv2.imshow('img', img)
# #cv2.imshow('edge', img_edge)
# #cv2.imshow('edge_d', img_edge_d)
# #cv2.imshow('edge_e', img_edge_e)
# cv2.waitKey(0)