'''
#Created by: Jack Cornwall
#Email: jackcornwall91@gmail.com
#Git hub: https://github.com/JackDCornwall
#Website:https://jackcornwall.co.uk/

#Project: Virtual paint
#Date: 05.06.21
#Description: Using a webcam to pick up different coloured pens and trace a colour on the screen
Settings from Color_picker_060621.py:
Green bic pen lid: Hue min: 47 | Hue max: 73 | Sat min: 40 | Sat max: 88 | Val min: 44 | Val max: 255
Red bic pen lid: Hue min: 168 | Hue max: 179 | Sat min: 112 | Sat max: 201 | Val min: 130 | Val max: 255
Blue bic pen lid: Hue min: 102 | Hue max: 115 | Sat min: 149 | Sat max: 226 | Val min: 118 | Val max: 255
Purple bic pen lid: Hue min: 118 | Hue max: 132 | Sat min: 63 | Sat max: 153 | Val min: 148 | Val max: 255
'''

#importing required packages
import cv2
import numpy as np

#setting width and frame of our height
frameWidth = 640
frameHeight = 480

#importing webcam
cap = cv2.VideoCapture(0) #0 is the default webcam of the device

#settings for video capture
cap.set(3, frameWidth) #setting width
cap.set(4, frameHeight) #setting height
cap.set(10, 130) #setting brightness

#mask values in the following order:
#Hue min|Hue max|Sat min|Sat max|Val min|Val max
green = [47,73,40,88,44,255]
red = [168,179,112,201,130,255]
blue = [102,115,149,226,118,255]
purple = [118,132,63,153,148,255]

#list of all mask values to iterate through
my_colours = np.array([green, red, blue, purple])
col_names = ["green","red","blue","purple"]

#function to find colours
def findColours(img,colors):

    #converting input image to HSV colorspace
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #required to subset colors
    min_vals = [True,False,True,False,True,False]
    max_vals = [False,True,False,True,False,True]

    #running through each color

    count = 0 #counter to run through colour names
    for color in colors:


        #setting mask values taken from description above and found with Color_picker
        lower = np.array(color[min_vals])
        upper = np.array(color[max_vals])

        #creating mask using trackbar values
        mask = cv2.inRange(imgHSV,lower,upper)

        #displaying mask for testing purposes
        cv2.imshow(str(col_names[count]),mask)

        count = count + 1 #iterating counter

#runnign webcam until q is pressed
while True:
    #importing webcam feed frame to img
    success, img = cap.read()

    cv2.imshow("Result",img) #dispaying image frame in "Results window"
    findColours(img,my_colours) #running function to capture colours

    #creating escape
    if cv2.waitKey(1) % 0xFF == ord("q"):
        break