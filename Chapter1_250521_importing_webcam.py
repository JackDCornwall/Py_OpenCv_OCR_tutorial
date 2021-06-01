# importing required packages
import cv2

print("Package imported")  # confirming package has imported

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