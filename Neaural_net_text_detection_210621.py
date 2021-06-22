'''
#Created by: Jack Cornwall
#Email: jackcornwall91@gmail.com
#Git hub: https://github.com/JackDCornwall
#Website:https://jackcornwall.co.uk/

#Project: Neural network text detection trainer
#Date:21.06.21
#Description: Running through this tutorial: https://www.youtube.com/watch?v=y1ZrOs9s2QA
#Images can be found here: https://www.kaggle.com/scolianni/mnistasjpg or http://yann.lecun.com/exdb/mnist/ in raw form
'''
import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split

#####################----Settings----#####################
path = "Training Data/trainingSet/TesttrainingSet" #for quicker testing (25 images per file)
#path = "Training Data/trainingSet/trainingSet" #for full set
test_ratio = 0.2 #test fraction
valid_ratio = 0.05 #validation fraction
##########################################################

#listing all available directories
dir_list = os.listdir(path)

#extracting the number of classes to train
num_class = len(dir_list)

#creating empty img to store img data
img_array_list = [] #image BGR arrays will be stored here sequentially
img_cat_list = [] #image value will be store here (correct answer)
#the index for img_list and img_car_list will correspond to each other, however a DF could be used for this

#printing system update
print("Total folders detected:",num_class) #class counnt
print(" ") #formatting nicely
print("Currently importing folder number:") #header

#looping through each folder
for dir in dir_list:

    #path to images
    dir_path = path +"/" + dir

    #extracting a list of all images in
    img_list = os.listdir(dir_path)

    for img in img_list:

        img_path = dir_path+"/"+img

        #reading in current image array with OpenCV
        img_array = cv2.imread(img_path)

        #appending data
        img_array_list.append(img_array) #appending entire BGR array as list item
        img_cat_list.append(int(dir)) #appening digit number as int, folder names must be numbers (correct answer)

    #printing progress update
    print(dir, end=" ")
print(" ") #for formatting

#converting lists into numpy arrays
img_array_list = np.array(img_array_list)
img_cat_list = np.array(img_cat_list)

#checking we have arrays of the desired shape
#print(img_array_list.shape)
#print(img_cat_list.shape)

###Splitting data into train/test/validation
#splitting all data into train and test
img_train,img_test,cat_train,cat_test = train_test_split(img_array_list,img_cat_list,test_size = test_ratio)
#splitting remaining training data into train and validation
img_train,img_valid,cat_train,cat_valid = train_test_split(img_train,cat_train,test_size = valid_ratio)

#system message
print("Training data split:")
print("Training array size:",img_train.shape)
print("Test array size:",img_test.shape)
print("Validation array size:",img_valid.shape)

#running through each number and ensuring there is sufficient examples of it
for dir in dir_list:

    #printing system message to enesure we are happy with number of training images per digit
    print("For folder",dir,"there are:",len(np.where(cat_train == int(dir))[0]),"training images")
    #this again will only work if folders are digits

#end of code
print("Code has run successfully")