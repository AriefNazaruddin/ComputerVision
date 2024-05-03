import cv2

# read webcam

webcam = cv2.VideoCapture(0)


# visualize webcam

while True:
    ret, frame = webcam.read()

    img_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2LUV)

    cv2.imshow('frame', img_hsv)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()