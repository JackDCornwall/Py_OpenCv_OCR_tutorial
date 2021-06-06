'''
#Created by: Jack Cornwall
#Email: jackcornwall91@gmail.com
#Git hub: https://github.com/JackDCornwall
#Website:https://jackcornwall.co.uk/

#Project: Virtual paint
#Date: 05.06.21
#Description: Using a webcam to pick up different coloured pens and trace a colour on the screen
'''

#importing required packages
import cv2

#setting width and frame of our height
frameWidth = 640
frameHeight = 480

#importing webcam
cap = cv2.VideoCapture(0) #0 is the default webcam of the device

#settings for video capture
cap.set(3, frameWidth) #setting width
cap.set(4, frameHeight) #setting height
cap.set(10, 130) #setting brightness

#difining a function to find color
def findColor(img):

    #converting image to HSV space
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    cv2.show("HSV",imgHSV)


#runnign webcam until q is pressed
while True:
    #importing webcam feed frame to img
    success, img = cap.read()

    cv2.imshow("Result",img) #dispaying image frame in "Results window"

    #creating escape
    if cv2.waitKey(1) % 0xFF == ord("q"):
        break