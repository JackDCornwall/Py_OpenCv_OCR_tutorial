# importing required packages
import cv2

print("Package imported")  # confirming package has imported

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

# Using while True allows for continual capture
while True:
    success, img = cap.read()  # read each frame
    cv2.imshow("Video",img)  # displaying frame

    # setting frame rate and break parameter
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break