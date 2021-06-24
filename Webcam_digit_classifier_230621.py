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
width = 480 #width of image to be read in
height = 480 #height of image from webcamq
TH = 0.8 #minimum detection threshold
############################################

#setting up capture device
capture = cv2.VideoCapture(0) #setting capture device
capture.set(3,width) #setting width
capture.set(4,height) #setting height

#importing saved model
model = models.load_model("Trained models/trained_model_E30_Mnist_230621.h5")

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

    img_out = np.copy(img_in) #creating a copy to overlay with text

    img = preProcess(img) #pre processing image
    img = img.reshape(1,28,28,1) #requires depth for pre processing

    #predicting class ID
    ID = int(model.predict_classes(img)) #extracting most likely answer
    predictions = model.predict(img) #extracting all probabilities
    prob = max(predictions[0]) #extracting the probability of the detected digit

    #checking for result confidence
    if prob>TH:

        #adding text overlay if confidence is high enough
        cv2.putText(img_out,
                    str(ID)+"   "+str(round(prob*100,1))+"%",
                    (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (125,0,255),
                    3
                    )

        #printing output if confidence is high enough
        print("Digit detected: ",ID," with a probability of: ",str(round(prob*100,2)),"%",sep="")


    cv2.imshow("Output", img_out)  # outputting image

    #break command
    if cv2.waitKey(1) &0xFF == ord("q"):
        break #ends loop

#success message
print("Code has run successfully!")