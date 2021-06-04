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

#calculating height of image
height = imgBGR.shape[0]

###---------- DETECTING WORDS ----------###
#creating config file
conf = r'--oem 3 --psm 6 outputbase digits'
#oem 3 is the default tesseract engine
#psm 6 assuumes a single uniform block of text
#more settings can be found here: https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc

#extracting words from file
boxes = pytesseract.image_to_data(imgRGB,config = conf)

#creating counter
count = 0
#this counter is required as the first row contains the table headers and we want to ignore this

#iterating through each box
#.splitlines is required as tesseract OCR function returns a string
for box in boxes.splitlines():

    #adding to counter
    count = count+1

    #skipping first low
    if count !=1:

        # box is an str and needs to be turned into a list
        #box = box.split("\t") #this doesnt work because it leaves the 12th column empty but still countable
        box = box.split() #this works because it removes "blanks"

        #iterating only through box's containing words
        if len(box)==12:

            #coordinates of bounding box
            #here the coordinates match those used by openCV not those seen in image to boxes
            x,y,w,h = int(box[6]),int(box[7]),int(box[8]),int(box[9])

            #drawing bounding box
            cv2.rectangle(imgBGR,(x,y),(w+x,h+y),(125,0,255),1)

            #adding text to image
            cv2.putText(imgBGR,box[11],(x,y+60),cv2.FONT_HERSHEY_SIMPLEX,1,(125,0,255),2)

#displaying result
cv2.imshow("Result",imgBGR)

cv2.waitKey(0) #indefinite delay