#loading required libraries
import cv2
import numpy as np

img = cv2.imread("Resources/Cards.jpg") # import image

#defining height and width of new image to be generated
width = 250
height = 350

#defining the 4 corner points as a numpy array of floats
#in the following order:
#1.top left
#2.top right
#3.bottom left
#4.bottom right
ptsOld = np.float32([[111,219],[287,188],[154,482],[352,440]])
#these are the points on the original image

#points to transform to on new image
ptsNew = np.float32([[0,0],[width,0],[0,height],[width,height]])
#These will be the coordinates that ptsOld are transformed into

#generatin transformation matrix
matrix = cv2.getPerspectiveTransform(ptsOld,ptsNew)

#transforming image (performing warp)
outputImg = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image",img) #displaying image
cv2.imshow("Warped image", outputImg)

cv2.waitKey(0) #indefinite delay




