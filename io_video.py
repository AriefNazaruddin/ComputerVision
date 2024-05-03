import os

import cv2

# read video
Video_path = os.path.join('.', 'data', 'video_of_funny_cat (1080p).mp4')

video = cv2.VideoCapture(Video_path)

# visualize video

ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(30)

video.release()
cv2.destroyAllWindows()