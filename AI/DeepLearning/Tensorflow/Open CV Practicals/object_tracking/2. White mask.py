import cv2
from tracker import *


cap = cv2.VideoCapture(r"D:\Education\Datascience\PYTHON_BIGINNER\AI\DeepLearning\Tensorflow\Open CV Practicals\object_tracking\highway.mp4")


# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)


while True:
    ret, frame = cap.read()
    
    mask = object_detector.apply(frame)
     
    
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    
    key = cv2.waitKey(30)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()