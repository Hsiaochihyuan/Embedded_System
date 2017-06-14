import sys
import cv2
import time
import Rpi.GPIO as GPIO

WIDTH = 640
HEIGHT = 320

def servo_control(angle):
    # Control servo based on desired angle

def distance_to_angle(x, y):
    # Convert distance between face centroid and frame center
    # to desired angle of servo
    angle = 0

    return angle

def face_detect(faceCascade, img):
    # Face detection algorithm
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    print "Found {0} faces!".format(len(faces))

    # Face position
    x_pos = []
    y_pos = []
    for (x, y, w, h) in faces:
        x_pos.append(x + w / 2)
        y_pos.append(y + h / 2)
        # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Centroid of faces
    x_centroid = sum(x_pos) / len(faces)
    y_centroid = sum(y_pos) / len(faces)
    print 'Centroid: ({}, {})'.format(x_centroid, y_centroid)

    return (x_centroid, y_centroid)

def main():
    # Cascading for face detection
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    
    # Video capture
    cap = cv2.VideoCapture(0)

    while True: 
        before = time.time()
        ret, frame = cap.read()

        cv2.imwrite('result.png', frame)
        img = cv2.imread('result.png')
        
        (x, y) = face_detect(faceCascade, img)
        angle = distance_to_angle(x, y)
        servo_control(angle)

if __name__ == "__main__":
    main()
