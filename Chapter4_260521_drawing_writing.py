#importing required packages
import cv2
import numpy as np

#making a black image (a matrix of zeroes)
black = np.zeros((512,512,3),np.uint8) #this is an BGR black image with 3 color channels
#np.uint8 makes the values possible between 0 and 255 (8 bit colours)
#black = np.zeros((512,512)) # This would simply make a grayscale black image

#colouring the whole image in different colours
blue = np.copy(black) #copying array
#for some reason simply using blue=black doesnt copy it just means they are always identical and doesn't work
blue[:] = 255,0,0 #turning on all blue pixels
#using [:] simply selects the full amount.

green = np.copy(black) #copying array
green[:] = (0,255,0) #turning on all green pixels

red = np.copy(black) #copying array
red[:] = (0,0,255) #turninblug on all red pixels

cyan = np.copy(black) #copying array
cyan[:] = (255,255,0) #turning on green and blue pixels

white = np.copy(black) #copying array
white[:] = (255,255,255) #turning on all pixels

#creating a square with coordinates
square = np.copy(black) #copying array
square[100:150,100:150] = (255,255,255) #defining coordinates to change character

#creating a rectangle outline using cv2
rectangle = np.copy(black)
cv2.rectangle(rectangle,(0,0),(250,350),(0,0,125),2) #Where the final argument (2) is the thickness of the outline
#cv2.rectangle(rectangle,(0,0),(250,350),(0,0,125),cv2.FILLED) #The rectangle an also be filled in if needed.

#creating a circle
circle = np.copy(white) #copying array
cv2.circle(circle,(28,350),200,(0,0,0),2) # this circle only partially fits on the image but it still works

#putting text on images
words = np.copy(white) #copying array
text = "This should be black text, I wonder what happens if it doesnt all fit on the screen" #defining text
text2 = "balls"
cv2.putText(words,text,(0,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2) #placing text on image
cv2.putText(words,text2,(0,300),cv2.FONT_HERSHEY_DUPLEX,2,(125,0,255),4) #placing more text with different settings

#creating lines
lines = np.copy(black) # duplicating array
cv2.line(lines,(0,0),(300,300),(0,255,0),1) #creating a line
lines[100:101,200:512] = (125,0,37) #straight line made up color (Essentially a thin rectangle, not good for diagonals)
cv2.line(lines,(12,45),(512,512),(255,0,255),3) #creating a thick line in magenta

#printing dimensions of black box
print("Dimensions of black box",black.shape)

#displaying image
cv2.imshow("Black image",black)
cv2.imshow("Blue image",blue)
cv2.imshow("Green image",green)
cv2.imshow("Red image",red)
cv2.imshow("Cyan image",cyan)
cv2.imshow("White image",white)
cv2.imshow("White square on black",square)
cv2.imshow("Three lines",lines)
cv2.imshow("Rectangle",rectangle)
cv2.imshow("Circle",circle)
cv2.imshow("Text",words)

cv2.waitKey(0) #delay indefinitely