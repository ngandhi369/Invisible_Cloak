import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened():
    check, bg = cap.read();
    if check:
        cv2.imshow("bgimage",bg)

        if cv2.waitKey(5)==ord('s'):
            cv2.imwrite("bgimage.jpg",bg)
            break

cap.release()
cv2.destroyAllWindows()
