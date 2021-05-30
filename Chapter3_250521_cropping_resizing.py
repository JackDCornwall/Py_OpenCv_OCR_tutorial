'''
Please note in OpenCv the positive x direction is to the right/east (the same as cartesian).
However the positive y direction is down/south (opposite to cartesian).
The origin (0,0) of an image is in the top left corner.
'''

#importing required packages
import cv2

#Importing image
img = cv2.imread("Resources/Lambo.png")
height = img.shape[0] #sto-ring height
width = img.shape[1] #storing width

print("Dimensions of orginal image:",img.shape) #printing image dimensions
#The output figures are in the following order: height, width and finally the number of colour channels (BGR)

#resizing images
imgLarge = cv2.resize(img,(width*2,height*2)) #making image twice as large
imgSmall = cv2.resize(img,(round(width/2),round(height/2))) #making image half as large
imgSkewed = cv2.resize(img,(height,width)) #Any dimensions can be used skewing the image

#checking shape of resized images
print("Dimensions of enlarged image:",imgLarge.shape)
print("Dimensions of shrunk image:",imgSmall.shape)
print("Dimension of skewed image:",imgSkewed.shape)

#cropping image
'''since images are just matrices we don't need to to use cv2 function to crop'''
imgCropped = img[0:200,200:500]
#we first define height and then width, this is the opposite to defining cv2 functions
print("Dimensions of cropped image:",imgCropped.shape)

cv2.imshow("Image",img) #displaying image
#cv2.imshow("Large image",imgLarge) #displaying large image
#cv2.imshow("Small image",imgSmall) #displaying small image
#cv2.imshow("Skewed image",imgSkewed) #displaying skewed image
cv2.imshow("Cropped image",imgCropped) #displaying cropped image

cv2.waitKey(0)#indefinite delay