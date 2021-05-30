#importing required packages
import cv2
import numpy as np

#reading image
img = cv2.imread("Resources/Lena.png") #importing image
img2 = cv2.imread("Resources/Einstein.jpg")

#converting to greyscale
img2Grey = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#resizing imgGrey
imgGreyResize = cv2.resize(imgGrey,(img2Grey.shape[1],img2Grey.shape[0]))

print("Dimensions of greyscale img2",img2Grey.shape) #checking image dimensions and color space
print("Dimensions of greyscale img",imgGrey.shape) #checking image dimensions and color space
print("Dimensions of resized greyscale img",imgGreyResize.shape) #checking image dimensions and color space

#combining two images
#imgCombo = np.hstack((img,img2Grey)) #This doesnt work as the images dont have the same number of color spaces
#imgCombo = np.hstack((imgGrey,img2Grey)) #This doesnt work as the images dont have the same dimensions
imgCombo = np.hstack((imgGreyResize,img2Grey))

#horrizontally and vertically stacking the lena image on top of itself (using numpy functions)
imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))
#for this to work they both need to be in the same colour space

#displaying images
#cv2.imshow("Image",img)
#cv2.imshow("Horizontally stacked",imgHor)
#cv2.imshow("Vertically stacked",imgVer)
cv2.imshow("Two different images stacked",imgCombo)

cv2.waitKey(0) #indefinite delay