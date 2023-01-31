import cv2
import numpy as np
from detection import orange_detection


camera_id = '/dev/video0'
cap = cv2.VideoCapture(camera_id, cv2.CAP_V4L2)
result = cv2.VideoWriter(
    'orange_detection.avi',
    cv2.VideoWriter_fourcc('M','J','P','G'),
    20,
    (300, 300) 
    )

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (300, 300))

    # video processing
    low_orange = np.array([11, 150, 90])
    high_orange = np.array([180, 255, 255])

    gaussian_blur = cv2.GaussianBlur(frame, (15, 15), 0)
    hsv = cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, low_orange, high_orange)
    kernel = np.ones((5, 5), np.int8)
    erosion = cv2.erode(mask, kernel, iterations=2)

    contours, _ = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    od = orange_detection(contours)
    x, y, x2, y2 = od
    cx = int((x + x2) / 2)
    cy = int((y + y2) / 2)

    print("cx = {}, cy = {}".format(cx, cy))


    # show output
    #cv2.rectangle(frame, (x, y), (x2, y2), (255, 0, 0), 4)
    cv2.circle(frame, (cx, cy), 20, (0, 0, 255), 4)
    cv2.imshow('frame', frame)
    result.write(frame)
    

    k = cv2.waitKey(5) & 0xFF
    if k == 27 or k == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
result.release()