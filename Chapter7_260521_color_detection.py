#importing required packages
import cv2

import numpy as np

#We need a function to pass into the trackbars
#However we wont be using it.
h_min,h_max,s_min,s_max,v_min,v_max,mask = 0,0,0,0,0,0,0

#not having a variable returns an error (description of function at the end of function)
def update(a):
    #Ensuring changes occur to variables outside of function
    global h_min,h_max,s_min,s_max,v_min,v_max,mask

    #updating variables as trackbar moves
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    #printing updates
    print("Hue min:",h_min,"| Hue max:",h_max,"| Sat min:",s_min,
          "| Sat max:",s_max,"| Val min:",v_min,"| Val max:",v_max
          )

    #updating mask every time values change
    #creating a mask in the range of the desired colours
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    #creating mask using trackbar values
    mask = cv2.inRange(imgHSV,lower,upper)

    cv2.imshow("Mask", mask) #drawing mask image
    #We can move the slide bars around affecting the white and black part of the image.
    #We can then use the rest of the software to detect the color of the white part.

path = "Resources/Lambo.png" #path to image

img = cv2.imread(path) #importing image

#Converting to HSV color space (Hue saturation value)
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#creating window with trackbars for real time tinkering
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240) # Resizing window (name needs to be consistent

''' 
#creating tweakable slidebars (Default values)
cv2.createTrackbar("Hue Min","TrackBars", 0, 179, update) #creating trackbars
#Arguments: Trackbar name, Window where they are to appear, min val, max val, function
cv2.createTrackbar("Hue Max","TrackBars", 179, 179, update) #creating trackbars
cv2.createTrackbar("Sat Min","TrackBars", 0, 255, update) #creating trackbars
cv2.createTrackbar("Sat Max","TrackBars", 255, 255, update) #creating trackbars
cv2.createTrackbar("Val Min","TrackBars", 0, 255, update) #creating trackbars
cv2.createTrackbar("Val Max","TrackBars", 255, 255, update) #creating trackbars
'''

#creating tweakable slidebars (Generating desired mask by default)
cv2.createTrackbar("Hue Min","TrackBars", 0, 179, update) #creating trackbars
#Arguments: Trackbar name, Window where they are to appear, min val, max val, function
cv2.createTrackbar("Hue Max","TrackBars", 24, 179, update) #creating trackbars
cv2.createTrackbar("Sat Min","TrackBars", 156, 255, update) #creating trackbars
cv2.createTrackbar("Sat Max","TrackBars", 255, 255, update) #creating trackbars
cv2.createTrackbar("Val Min","TrackBars", 120, 255, update) #creating trackbars
cv2.createTrackbar("Val Max","TrackBars", 255, 255, update) #creating trackbars

'''
#We can now continuosuly update the mask image with the values
while True:
    #creating a mask in the range of the desired colours
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    #creating mask using trackbar values
    mask = cv2.inRange(imgHSV,lower,upper)
'''

#displaying images
cv2.imshow("Original image",img)
cv2.imshow("HSV image",imgHSV)
update(0) #running update once so that the mask image is shown.
cv2.imshow("Mask",mask)

#taking only white pixels from mask out of img
imgOut = cv2.bitwise_and(img,img,mask=mask) #the above function checks where the pixels are both present and

cv2.imshow("Final Output",imgOut)

cv2.waitKey(0) #indefinite delay