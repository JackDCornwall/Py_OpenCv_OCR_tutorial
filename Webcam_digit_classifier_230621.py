'''
#Created by: Jack Cornwall
#Email: jackcornwall91@gmail.com
#Git hub: https://github.com/JackDCornwall
#Website:https://jackcornwall.co.uk/

#Project: Digit classifier
#Date:23.06.21
#Description: Uses a .p pickle file created by the script Neural_net_text_detection_210621.py and uses it to classify digits
Created following tutorial found here: https://www.youtube.com/watch?v=y1ZrOs9s2QA&t=3367s
The tutorial uses pickle to export/import the trained model, however keras
'''
#importing required packages
import numpy as np
import cv2
from keras import models

##############----SETTINGS----##############
width = 640
height = 480
############################################

#setting up capture device
capture = cv2.VideoCapture(0) #setting capture device
capture.set(3,width) #setting width
capture.set(4,height) #setting height

#importing saved model
model = models.load_model("Trained models/trained_model.h5")

#pre-processing function
def preProcess(img):

    #converting to greyscale
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #equalising image (distribute the lighting evenly)
    img = cv2.equalizeHist(img)

    return img #outputting processed image

#runnign camera
while True:

    success, img_in = capture.read() #importing captured image
    img = np.asarray(img_in) #converting image to a numpy array
    img = cv2.resize(img,(28,28)) #resizing image
    img = preProcess(img) #pre processing image
    img = img.reshape(1,28,28,1) #requires depth for pre processing

    #predicting class ID
    ID = int(model.predict_classes(img)) #extracting most likely answer
    predictions = model.predict(img) #extracting all probabilities
    prob = max(predictions[0])
    print(prob)


    #break command
    if cv2.waitKey(1) &0xFF == ord("q"):
        break #ends loop

#success message
print("Code has run successfully!")
