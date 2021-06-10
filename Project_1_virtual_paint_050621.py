'''
#Created by: Jack Cornwall
#Email: jackcornwall91@gmail.com
#Git hub: https://github.com/JackDCornwall
#Website:https://jackcornwall.co.uk/

#Project: Virtual paint
#Date: 05.06.21
#Description: Using a webcam to pick up different coloured pens and trace a colour on the screen
Settings from Color_picker_060621.py:
Green bic pen lid: Hue min: 70 | Hue max: 86 | Sat min: 46 | Sat max: 150 | Val min: 95 | Val max: 255
Light green bic pen lid: Hue min: 34 | Hue max: 55 | Sat min: 46 | Sat max: 104 | Val min: 74 | Val max: 255
Red bic pen lid: Hue min: 163 | Hue max: 175 | Sat min: 124 | Sat max: 215 | Val min: 172 | Val max: 255
pink bic pen lid: Hue min: 136 | Hue max: 169 | Sat min: 25 | Sat max: 94 | Val min: 190 | Val max: 255
Blue bic pen lid: Hue min: 80 | Hue max: 120 | Sat min: 120 | Sat max: 255 | Val min: 216 | Val max: 255
Light blue bic pen lid: Hue min: 83 | Hue max: 97 | Sat min: 33 | Sat max: 141 | Val min: 234 | Val max: 255
Purple marker pen lid: Hue min: 113 | Hue max: 125 | Sat min: 43 | Sat max: 108 | Val min: 159 | Val max: 255
However these will vary by lighting condition and camera used
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
green = [79,88,72,133,102,255]
red = [163,175,124,215,172,255]
light_blue = [88,105,86,148,250,255]
purple = [133,125,43,108,159,255]

#list of all mask values to iterate through
my_colours = np.array([green, red, light_blue, purple])
col_names = ["green","red","light blue","purple"]

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

        #extracting contours for mask
        getContours(mask)

        #displaying mask for testing purposes
        #cv2.imshow(str(col_names[count]),mask)

        count = count + 1 #iterating counter

    #getContours(mask)

#creating function that will get the bounding box of "on" pixels
def getContours(img):

    #extracting contours
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    #iterating through each contour
    for cnt in contours:

        #calculating contour area
        area = cv2.contourArea(cnt)

        #disregarding any small contour
        if area>500:

            #drawing contours
            cv2.drawContours(imgOut,cnt,-1,(255,0,0),3)

            #calculating perimeter
            peri = cv2.arcLength(cnt,True)

            #calculating approximate corners
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)

            #extracting contour boundary coordinates & size
            x,y,w,h = cv2.boundingRect(approx)

#continuously looping
while True:
    #importing webcam feed frame to img
    success, img = cap.read()

    #final output image
    imgOut = img.copy()

    findColours(img,my_colours) #running function to capture colours

    cv2.imshow("Result", imgOut)  # dispaying image frame in "Results window"

    #creating escape
    if cv2.waitKey(1) % 0xFF == ord("q"):
        break