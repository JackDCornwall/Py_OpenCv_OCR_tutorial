#importing required packages
import cv2

path = "Resources/Shapes.png" #path to image

#defining function to get contours
def getContours(img):

    # extracting contours & hierarchy
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #gathers the outermost contours

    #for each contour
    for cnt in contours:
        #calculating area
        area = cv2.contourArea(cnt)

        #filter condition to reduce noise (small areas)
        if area > 100:
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 3)  # Overlaying all contours onto image
            peri = cv2.arcLength(cnt,True) #calcualting the perimeter of our closed shapes
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #calculates the approximate corner points (0.02 value to be tweaked)
            #print(len(approx)) #prints out the number of corner points
            #(3 is triangle, 4 is rectangle/diamond, anything above 4 is a circle)
            objCor = len(approx) #storing number of corners
            x,y,w,h = cv2.boundingRect(approx) #x,y and width and height of each shape
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(255,255,0),2) #drawing bounding rectangle.

            aspRat = w/h #calculating aspect ratio

            #naming function
            def name(txt):
                cv2.putText(imgContour,txt,(x + w // 4, y + h // 2),cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 0),1)

            #categorizing shapes
            if objCor == 3:
                name("triangle") #identifying triangles

            #Categorizing squares
            elif objCor == 4 and aspRat > 0.95 and aspRat < 1.05:
                name("square")

            #Categorizing rectangles
            elif objCor == 4:
                name("rectangle")

            #Categorizing circles
            elif objCor > 4:
                name("circle")

img = cv2.imread(path) #importing shapes image
imgContour = img.copy() #Creating a copy of the original image so that contours can be overlain

#converting to grey scale and adding blur
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(7,7),1)

#using canny function to find edges
imgCanny = cv2.Canny(imgBlur,100,100)

#running function
getContours(imgCanny)

#displaying image
cv2.imshow("Shapes image",img)
cv2.imshow("Processed image",imgContour)

cv2.waitKey(0) #indefinite delay