import cv2
import numpy

capture = cv2.VideoCapture('file.mp4')

if (capture.isOpened()==False):
    print("error Opening file")

while (capture.isOpened()):

    ret,frame = capture.read()
    if ret == True:
        cv2.imshow("Frame",frame)
        if cv2.waitKey(25) & 0xFF==ord('q'):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()