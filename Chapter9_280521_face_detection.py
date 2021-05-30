#importing required libraries
import cv2

#importing HAR cascade file
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

img = cv2.imread("Resources/Team.jpg") #importing image

#converting to greyscale
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detecting faces
faces = faceCascade.detectMultiScale(imgGrey,1.1,4)
#This creates an array containing arrays with x,y,w,h for each

#iterating through each face found to draw bounding box
for face in faces:
    x,y,w,h = face[0],face[1],face[2],face[3] #extracting bounding box dimensions

    #calculating area
    area = x*y

    #drawing bounding box on original image
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)

#extracting dimensions of original image
width = img.shape[1]
height = img.shape[0]
#resizing image
img = cv2.resize(img,(round(width*.25),round(height*.25)))


#displaying images
cv2.imshow("Results",img)

cv2.waitKey(0) #adding indefinite delay

