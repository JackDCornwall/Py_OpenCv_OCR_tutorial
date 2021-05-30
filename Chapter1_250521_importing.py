# importing required packages
import cv2

print("Package imported")  # confirming package has imported

'''
##----------IMPORTING IMAGE----------##
#importing image
img = cv2.imread("Resources/Lena.png")

#displaying imageq
cv2.imshow("Output",img) #First argument names window and second is image we want to show.
#The image will just flash up for an instant unless we add the following delay
cv2.waitKey(0) #0 is an infinite delay, otherwise we can input the number of milliseconds desired
'''

'''
##----------VIDEO IMPORT----------##

#importing video
vid = cv2.VideoCapture("Resources/sample-mp4-file.mp4")

#loops through video frame by frame
while True:
    success, img = vid.read() #tells us if each individual frame was captured (T/F) and then stores that frame as an image
    cv2.imshow("Video",img) #displays image

    #plays video at a given rate but also stops the code running on keystroke
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    #cv2.waitKey(50) #adds delay betweeen frames
'''

##----------WEBCAM VIDEO----------##

# Importing webcam footage is the same as importing video
cap = cv2.VideoCapture(0)  # 0 simply refers to the default webcapture device, otherwise an ID can be specified.

# specifying settings for video capture
cap.set(3,640) #capture setting 3 is the width of the video in px
cap.set(4,480) #capture setting 4 is the height of the video in px
cap.set(10,1000) #capture setting 10 is the brightness

# Using while True allows for continual capture
while True:
    success, img = cap.read()  # read each frame
    cv2.imshow("Webcam",img)  # displaying frame

    # setting frame rate and break parameter
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break