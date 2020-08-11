import cv2
import numpy as np

cap = cv2.VideoCapture(0)
bg = cv2.imread('./bgimage.jpg')

while cap.isOpened():
    check, frame = cap.read()
    if check:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # the given limit is for cyan color
        l_cyan = np.array([72,70,70])
        u_cyan = np.array([115,255,255])

        mask = cv2.inRange(hsv,l_cyan,u_cyan)

        part1 = cv2.bitwise_and(bg,bg,mask=mask)

        mask = cv2.bitwise_not(mask)

        part2 = cv2.bitwise_and(frame,frame,mask=mask)

        cv2.imshow("Final",part1+part2)

        if cv2.waitKey(5) == ord('s'):
            break


cap.release()
cv2.destroyAllWindows()
