import cv2
import numpy as np

camera_id = '/dev/video0'
cap = cv2.VideoCapture(camera_id, cv2.CAP_V4L2)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_orange = np.array([11, 150, 90])
    high_orange = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, low_orange, high_orange)
    result = cv2.bitwise_and(frame, frame, mask=mask) 

    #gaussian_blur = cv2.GaussianBlur(result, (15, 15), 0)
    median_blur = cv2.medianBlur(result, 15, 0)
    kernel = np.ones((5, 5), np.int8)
    # erosion = cv2.erode(mask, kernel, iterations=1)
    # dilation = cv2.dilate(mask, kernel, iterations=1)

    # open = remove false positives
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
 
    #cv2.imshow('mask', mask) 
    #cv2.imshow('result', result) 
    # cv2.imshow('erosion', erosion)
    #cv2.imshow('dilation', dilation)
    #cv2.imshow('opening', opening)
    #cv2.imshow('closing', closing)
    #cv2.imshow('gaussian_blur', gaussian_blur)
    #cv2.imshow('median_blur', median_blur)

    box = (0, 0, 0, 0)
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        box = (x, y, x + w, y + h)

    x, y, x2, y2 = box
    cv2.rectangle(frame, (x, y), (x2, y2), (255, 0, 0), 4)
    cv2.imshow('frame', frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27 or k == ord('q'):
        break

cv2.destroyAllWindows()
cap.release( )