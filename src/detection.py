import cv2
import numpy as np


def orange_detection(contours):
    box = (0, 0, 0, 0)
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        box = (x, y, x + w, y + h)
        break
        
    return box