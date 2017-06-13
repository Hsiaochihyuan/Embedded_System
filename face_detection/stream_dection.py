import sys
import cv2
import time
import numpy as np

cascPath = "haarcascade_frontalface_default.xml"

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cascPath)

while True: 
    before = time.time()
    ret, frame = cap.read()

    cv2.imwrite('result.png', frame)
    img = cv2.imread('result.png')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imwrite('detect.png', img)

cap.release()


















