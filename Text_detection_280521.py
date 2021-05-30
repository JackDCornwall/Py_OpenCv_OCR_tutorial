#importing required libraries
import cv2
import pytesseract

#pointing to our OCR tesseract install
pytesseract.pytesseract.tesseract_cmd = "C://Users/Jack/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"

imgBGR = cv2.imread("Resources/test_text_2.png") #importing image to read

#pytesseract only accepts RGB images and openCV is BGR by default
#converting image to RGB
imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)

#using pytesseract OCR functions
#print(pytesseract.image_to_string(imgRGB)) #prints detected text
#print(pytesseract.image_to_boxes(imgRGB)) #prints dimensions of character bounding boxes
boxes = pytesseract.image_to_boxes(imgRGB)
#print(type(boxes)) #boxes is just a string of data that divided with newlines and spaces so boxes.splitlines to be used

#calculating height of image
height = imgBGR.shape[0]

'''###---------- DETECTING CHARACTERS ----------###

#iterating through each box
#.splitlines used because image to boxes returns list not array.

for box in boxes.splitlines():

    #print(type(boxes)) #box is just a string separated by spaces and split needs to be used
    #divinding boxes up sensibly
    box = box.split(" ") #this should now be converted into a usable list


    #extracting bouding box
    
    x,y,w,h = int(box[1]),height-int(box[2]),int(box[3]),height-int(box[4])
    # values returned arent quite in the format we would expect (y axis is inverted

    #adding bounding box to original image
    cv2.rectangle(imgBGR,(x,y),(w,h),(0,255,0),1)
    #normally we would have to add the x & y to the second coordinate, however tesseract outputs this already calculated

    #adding character to image (+15 is added to offset text from box)
    cv2.putText(imgBGR,box[0],(x,y+15),cv2.FONT_HERSHEY_SIMPLEX,.5,(125,0,255),2)
'''

###---------- DETECTING WORDS ----------###
#extracting words from file
boxes = pytesseract.image_to_data(imgRGB)

#iterating through each box
#.splitlines is required as tesseract OCR function returns a string
for box in boxes.splitlines():

    #box is an str and needs to be turned into a list
    box = box.split("\t")

    print(box)


#displaying result
cv2.imshow("Result",imgBGR)

cv2.waitKey(0) #indefinite delay