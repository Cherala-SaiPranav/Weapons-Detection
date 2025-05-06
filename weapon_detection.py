import imutils
import numpy as np
import cv2

gun_cascade = cv2.CascadeClassifier("cascade.xml")
cam = cv2.VideoCapture(0)

firstFrame = None
gun_exist = False

while True:
    ret, frame = cam.read()

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gun = gun_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100))

    if len(gun) > 0:
        gun_exist = True


    for (x, y, w, h) in gun:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF

    if gun_exist:
        print("Weapon Detected.")
    else:
        print("No Weapons Detected.")

    if key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
