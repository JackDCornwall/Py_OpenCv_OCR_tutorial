# importing required packages
import cv2

print("Package imported")  # confirming package has imported


##----------IMPORTING IMAGE----------##
#importing image
img = cv2.imread("Resources/Lena.png")

#displaying image
cv2.imshow("Output",img) #First argument names window and second is image we want to show.
#The image will just flash up for an instant unless we add the following delay
cv2.waitKey(0) #0 is an infinite delay, otherwise we can input the number of milliseconds desiredd