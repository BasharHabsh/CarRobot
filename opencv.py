import serial
import time
import cv2
import numpy as np


url = 'http://192.168.43.135:8080/video'

cap = cv2.VideoCapture(url)
arduino = serial.Serial('COM3', 9600, timeout=1)

x=0
y=0

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask3 = mask1+mask2
    maskeli = cv2.bitwise_and(frame,frame,mask=mask3)
    contours, hierarchy = cv2.findContours(mask3, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if(area > 300):
            x,y,w,h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),10)
            durum=""
            if(x>210 and x<400 and y >350):
                durum="back"
                arduino.write(b'b')
            elif(x>210 and x<400 and y< 90):
                durum="front"
                arduino.write(b'f')
            elif(y>90 and y<350 and x < 210):
                durum="left"
                arduino.write(b'l')
            elif(y>90 and y<350 and x > 400):
                durum="right"
                arduino.write(b'r')
            else:
                durum=""
                arduino.write(b's')
            cv2.putText(frame, durum , (10,50), cv2.FONT_ITALIC,2, 100,5,5)
            print(durum)
        """else:
            durum="dur"
            arduino.write("*0000".encode())
            cv2.putText(frame, durum , (10,50), cv2.FONT_ITALIC,2, 100,5,5)
            print(durum)"""

    cv2.imshow("filtreli", maskeli)
    cv2.imshow("ana ekran", frame)
    #print(x,y)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
cap.release()