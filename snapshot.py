import cv2
import numpy as np

def TakeSnapAndSave():
    cap = cv2.VideoCapture(0)

    ret, img = cap.read()   

    cv2.imwrite('resources/snapshot.jpg',img)
    
    cap.release()
    cv2.destroyAllWindows()

# TakeSnapAndSave()