'''
#Created by: Jack Cornwall
#Email: jackcornwall91@gmail.com
#Git hub: https://github.com/JackDCornwall
#Website:https://jackcornwall.co.uk/

#Project: Virtual paint
#Date: 05.06.21
#Description: Using a webcam to pick up different coloured pens and trace a colour on the screen
Settings from Color_picker_060621.py vary to much to annotate based on light source (window open/time of day),
room we are in or even webcam, these should be gathered at the start of each run
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
green = [74,87,106,146,86,198]
red = [167,177,116,204,174,255]
light_blue = [75,110,111,168,236,251]
purple = [111,125,41,127,163,255]

#color values to be drawn
color_values = [
    [0,255,0],
    [0,0,255],
    [255,255,0],
    [255,0,255]
]

#list of all mask values to iterate through
my_colours = np.array([green, red, light_blue, purple])
col_names = ["green","red","light blue","purple"]

#function that extracts colors
def findColours(img,colors,color_vals):

    #converting input image to HSV colorspace
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    count = 0 #setting counter to zero which will loop through BGR colour values

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
        x,y = getContours(mask) #we are also getting returned tip of pen points

        #now we can draw a circle around those values and draw in on image results
        cv2.circle(imgOut,(x,y),10,color_vals[count],cv2.FILLED)

        #displaying mask for testing purposes
        #cv2.imshow(str(col_names[count]),mask)

        count = count + 1 #iterating counter

    #getContours(mask)

#creating function that will get the bounding box of "on" pixels
def getContours(img):

    #extracting contours
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    # returning zeroes in case nothing is detected (this needs to be run before the if statement)
    x, y, w, h = 0, 0, 0, 0

    #iterating through each contour
    for cnt in contours:

        #calculating contour area
        area = cv2.contourArea(cnt)

        #disregarding any small contour
        if area>300:

            #drawing contours
            #cv2.drawContours(imgOut,cnt,-1,(255,0,0),3) #this is commented out once we know we are detecting it propperly

            #calculating perimeter
            peri = cv2.arcLength(cnt,True)

            #calculating approximate corners
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)

            #extracting contour boundary coordinates & size
            x,y,w,h = cv2.boundingRect(approx)


    #returning the value of the tip
    return x+(w//2),y

#continuously looping
while True:
    #importing webcam feed frame to img
    success, img = cap.read()

    #final output image
    imgOut = img.copy()

    findColours(img,my_colours,color_values) #running function to capture colours

    cv2.imshow("Result", imgOut)  # dispaying image frame in "Results window"

    #creating escape
    if cv2.waitKey(1) % 0xFF == ord("q"):
        break