'''
#Created by: Jack Cornwall
#Email: jackcornwall91@gmail.com
#Git hub: https://github.com/JackDCornwall
#Website:https://jackcornwall.co.uk/

#Project: Color picker
#Date: 06.06.21
#Description: Uses a HSV mask to select a color from a webcam. It is an improved version of the code in chapter 7
#and required for Project 1 virtual paint.
'''
#importing required packages
import cv2
import numpy as np

cv2.imread("Resources/Lambo.png")

#function to call when updating trackbars
def update(a): # all fuunctions need a variable however nothing is passed in here
    #Ensuring changes occur to variables outside of function
    global h_min,h_max,s_min,s_max,v_min,v_max,mask

    #updating variables as trackbar moves
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
    #printing updates
    print("Hue min:",h_min,"| Hue max:",h_max,"| Sat min:",s_min,
          "| Sat max:",s_max,"| Val min:",v_min,"| Val max:",v_max
          )

    #updating mask every time values change
    #creating a mask in the range of the desired colours
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    # Using while True allows for continual capture
    while True:
        success, img = cap.read()  # read each frame

        # converting image into HSV color space
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # creating mask using trackbar values
        mask = cv2.inRange(imgHSV, lower, upper)

        cv2.imshow("BGR output", img)  # displaying raw frames from webcam
        cv2.imshow("HSV Output", imgHSV)  # displaying HSV image

        cv2.imshow("Mask", mask)  # drawing mask image
        # We can move the slide bars around affecting the white and black part of the image.
        # We can then use the rest of the software to detect the color of the white part.

        #cutting around masked image
        imgOut = cv2.bitwise_and(img, img, mask=mask) #creating output image only showing allowed colours

        #displaying output image
        cv2.imshow("Output image",imgOut)

        # setting frame rate and break parameter
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

#creating trackbar window
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240) #resizing the trackbars
cv2.createTrackbar("Hue Min","Trackbars",0,179,update) #179 is the maximum hue value in open CV, function to update
cv2.createTrackbar("Hue Max","Trackbars", 179, 179, update)
cv2.createTrackbar("Sat Min","Trackbars", 0, 255, update)  #maximum value for sat is 255
cv2.createTrackbar("Sat Max","Trackbars", 255, 255, update)
cv2.createTrackbar("Val Min","Trackbars", 0, 255, update)  #maximum value for for value is 255
cv2.createTrackbar("Val Max","Trackbars", 255, 255, update)
#create trackbars arguments: Var name, window to edit, current/initial value,max value

# Importing webcam footage is the same as importing video
cap = cv2.VideoCapture(0)  # 0 simply refers to the default webcapture device, otherwise an ID can be specified.

# specifying settings for video capture
cap.set(3,640) #capture setting 3 is the width of the video in px
cap.set(4,480) #capture setting 4 is the height of the video in px
cap.set(10,1000) #capture setting 10 is the brightness

#initiating first update call so that function runs
update(0)