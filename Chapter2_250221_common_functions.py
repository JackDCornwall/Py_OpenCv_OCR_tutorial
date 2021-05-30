#importing required packages
import cv2
import numpy as np

#importing image
img = cv2.imread("Resources/Lena.png")

#converting to greyscale
#cvtColor converts between colour spaces, openCV uses BGR by default not RGB
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #COLOR_BGR2GRAY converts images to greyscale

#adding gaussian blur
#imgBlur7 = cv2.GaussianBlur(img,(7,7),0) #The matrix here must be made up of odd numbers and represents the kernel
#imgBlur43 = cv2.GaussianBlur(img,(43,43),0) #The larger the matrix, the more blurred the image will be
#final variable is sigma zero, out of the scope of this example.

#edge detector using Canny function
imgCanny = cv2.Canny(img,100,100) #This requires threshold parameters (we are using 100 and 100)
imgCannyHigh = cv2.Canny(img,10000,10000) #This is a high threshold image
imgCannyLow = cv2.Canny(img,10,10) #This uses a low threshold
#The threshold can be used to set how agressive the edge detection is

#dialation (opposite of erosion) (For example Canny edges can be increased)
kernel = np.ones((5,5),np.uint8) #creating a matrix of 1 with size 5x5
#np.uint8 simply means the matrix is storing unsigned integers with 8 bits (range from 0 to 255)
imgDilated = cv2.dilate(imgCanny, kernel, iterations = 1)
#Here again we need to use a matrix kernel, in this case we need a matrix that has all 1 values but with a specific size
#This is one application of dialation, however it can be used on non edge images.
#we can increase the thickness by adding more passes (increasing iterations)

#erosion (opposite of dilation)
imgEroded = cv2.erode(imgDilated, kernel, iterations = 1)

#opening all images
cv2.imshow("Original image",img) #opening original image

#cv2.imshow("Greyscale image",imgGrey) #showing the greyscale image

#cv2.imshow("Blurred image 7",imgBlur7) #displaying slightly blurred image
#cv2.imshow("Blurred image 43",imgBlur43) #displaying very blurred image

cv2.imshow("Edge image",imgCanny) #displaying edge detection image
#cv2.imshow("Edge image HT",imgCannyHigh) #displaying edge detection image with high detection threshold
#cv2.imshow("Edge image LT",imgCannyLow) #displaying edge detection image with low detection threshold

cv2.imshow("Dialated edge image", imgDilated) #displaying dilated Canny image

cv2.imshow("Eroded image", imgEroded) #isplaying eroded image

cv2.waitKey(0) #indefinite delay