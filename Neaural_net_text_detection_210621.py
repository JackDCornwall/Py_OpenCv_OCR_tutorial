'''
#Created by: Jack Cornwall
#Email: jackcornwall91@gmail.com
#Git hub: https://github.com/JackDCornwall
#Website:https://jackcornwall.co.uk/

#Project: Neural network text detection trainer
#Date:21.06.21
#Description: Running through this tutorial: https://www.youtube.com/watch?v=y1ZrOs9s2QA
#Images can be found here: https://www.kaggle.com/scolianni/mnistasjpg or http://yann.lecun.com/exdb/mnist/ in raw form
The tutorial uses pickle to export/import the trained model, however keras model.save models.load_model
'''
#importing require packages
import numpy as np
import cv2
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Dropout,Flatten,Dense
from keras.layers.convolutional import Conv2D, MaxPooling2D
# import pickle

os.add_dll_directory("C://Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.4")
# added this line based on this page:https://github.com/tensorflow/tensorflow/issues/48868

#####################----Settings----#####################
#path = "Training Data/trainingSet/TesttrainingSet" #for quicker testing (25 images per file)
path = "C://Users/conta/Documents/python/Training data/Merged_test/" #for full set
test_ratio = 0.1 #test fraction
valid_ratio = 0.05 #validation fraction

#declaring model training parameters
batch = 50 #batch size from dataGen
epoch = 10 #number of Epochs
steps = None #steps per epoch set to None, the epoch will run until the dataset is exhausted.

##########################################################

#defining function to preprocess images
def preProcess(img):

    #converting to greyscale
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #checking if image is 32x32 if not resizing.
    if (img.shape[0] != 32) or (img.shape[1] != 32):

        img = cv2.resize(img , (32 , 32)) #reshaping image if required

    #equalising image (distribute the lighting evenly)
    img = cv2.equalizeHist(img)

    return img #outputting processed image

#defining training model using LeNet Convolutional Neural Network
def LeNet_Model():

    #these parameters will be required to train model
    noOfFilters = 60
    sizeOfFilter1 = (5,5)
    sizeOfFilter2 = (3,3)
    sizeOfPool = (2,2)
    noOfNodes = 500

    model = Sequential()

    #adding first convolutional layer
    model.add((Conv2D(noOfFilters,
                      sizeOfFilter1,
                      input_shape = (32,32,1),
                      activation = "relu"
                      )))

    #adding second convolutional layer (no need to specify dimensions/shape again
    model.add((Conv2D(noOfFilters,sizeOfFilter1,input_shape = (32,32,1),activation = "relu")))

    #adding pooling layer
    model.add(MaxPooling2D(pool_size=sizeOfPool))

    #adding third convolutional layer (with half the number of filters and smaller filters)
    model.add((Conv2D(noOfFilters//2,sizeOfFilter2,input_shape = (32,32,1),activation = "relu")))

    #adding 4th convolutional layer
    model.add((Conv2D(noOfFilters//2,sizeOfFilter2,input_shape = (32,32,1),activation = "relu")))

    #adding another pooling layer
    model.add(MaxPooling2D(pool_size=sizeOfPool))

    #adding dropout layer (these help reduce overfitting making the model more generic)
    model.add(Dropout(0.5))

    #Adding flaten layer
    model.add(Flatten())

    #Adding dense layer
    model.add(Dense(noOfNodes,activation="relu"))

    #adding dropout layer
    model.add(Dropout(0.5))

    #Adding final dense layer with the number of classes and softmax activation
    model.add(Dense(num_class,activation="softmax"))

    #compiling  with Adam optimizer (lr = learning rate
    model.compile(Adam(learning_rate=0.0001),loss="categorical_crossentropy",metrics=["accuracy"])

    #returning model
    return model

# #viewing an example pre processed image
# test_img = cv2.imread(path+"/0/img_4.jpg") #importing test imagemg
# test_img = cv2.resize(test_img,(200,200))#resizing image so it is usable
# cv2.imshow("Image before processing",test_img) #displaying unprocessed image
# cv2.imshow("Preprocessed image",preProcess(test_img)) #displaying processed image
# cv2.waitKey(0)

##################################################################################################################

#listing all available directories
dir_list = os.listdir(path)

#extracting the number of classes to train
num_class = len(dir_list)

#creating empty img to store img data
img_array_list = [] #image BGR arrays will be stored here sequentially
img_cat_list = []#image value will be store here (correct answer)

cat_data = pd.DataFrame(columns = ["img","cat","cat_no"])# empty dataframe that will store img_array, category, category_number #TODO update

cat_map = pd.DataFrame(columns = ["cat","cat_no"]) # category number mapping for vlookup purposes #TODO update

#the index for img_list and img_car_list will correspond to each other, however a DF could be used for this

#printing system update
print("Total folders detected:",num_class) #class count
print(" ") #formatting nicely
print("Currently importing & pre-processing folder number:") #header

#creating inxed number for cat_map creation
index_no = 0

#looping through each folder
for dir in dir_list:

    #path to images
    dir_path = path + dir

    #extracting a list of all images in
    img_list = os.listdir(dir_path)

    for img in img_list:

        img_path = dir_path+"/"+img

        #reading in current image array with OpenCV
        img_array = cv2.imread(img_path)

        #inverting colors of image
        #img_array = 255-img_array
        #this is required if images have inverted colours (i.e. original NMIST download with white chars on black background)

        #pre-processing image array as they are looped through
        img_array = preProcess(img_array)

        #attempting to debug
        if (img_array.shape != (32,32)):

            print(img_array.shape)
            print(img_path)

        #appending data
        img_array_list.append(img_array) #appending entire BGR array as list item
        img_cat_list.append(dir) #appening digit number as int, folder names must be numbers (correct answer)

        #creating line to append to cat_data
        cat_data_append = pd.DataFrame([[img_array,dir,index_no]],columns = ["img","cat","cat_no"])

        #appending row to cat_data
        cat_data = cat_data.append(cat_data_append)

    cat_map_append = pd.DataFrame([[dir,index_no]],columns = ["cat", "cat_no"]) #creating data that needs to be appended to cat_map

    cat_map = cat_map.append(cat_map_append) #appending to cat_map

    index_no = index_no + 1 # increasing index number

    #printing progress update
    print(dir, end=" ")
print(" ") #for formatting

#converting into lists and then numpy arrays (this is due to archaic issues caused by initially using lists before df)
img_array_list_old = np.array(img_array_list) #TODO these lines and thlose required to create them can be retroactively removed
img_cat_list_old = np.array(img_cat_list) #TODO these lines and thlose required to create them can be retroactively removed
img_array_list = np.array(list(cat_data["img"]))
img_cat_list = np.array(list(cat_data["cat_no"]))

#adding depth
array_shape = img_array_list.shape #extracting shapimg
img_array_list = img_array_list.reshape(array_shape[0],array_shape[1],array_shape[2],1) #reshaping array (adding depth)
#the neural network requires the extra dimension

#checking we have arrays of the desired shape
# print(img_array_list.shape)
# print(img_cat_list.shape)

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

#list to store training category names
categories = []

#running through each number and ensuring there is sufficient examples of it
for cat in list(cat_map["cat_no"]):

    #printing system message to enesure we are happy with number of training images per digit
    print("For category",cat,"there are:",len(np.where(cat_train == cat)[0]),"training images")
    #this again will only work if folders are digits

    #storing individual category names
    categories.append(cat)

#calculating number of categories
cat_len = len(categories)

#function to skew images so training becomes moreo general
dataGen = ImageDataGenerator(
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.2,
    shear_range=0.1,
    rotation_range=10 #degrees
)

#performing "skewing"
dataGen.fit(img_train)
#TODO cat_train requires only ints at this point
#converting folder dirs to training categories
cat_train = to_categorical(cat_train,cat_len)
cat_test = to_categorical(cat_test,cat_len)
cat_valid = to_categorical(cat_valid,cat_len)
### categories have to be integers

#creating model
model = LeNet_Model()
print(model.summary())

#generating training set
training_set = dataGen.flow(img_train,cat_train,batch_size=batch)

#running the training using fit generator (in batches using images from dataGen)
history = model.fit(training_set,
                    steps_per_epoch=steps,
                    epochs = epoch,
                    validation_data = (img_valid,cat_valid),
                    shuffle = 1
                                 )

#plotting loss over time
plt.figure(1)
plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])
plt.legend(["Training","Validation"])
plt.title("Loss")
plt.xlabel("Epoch")

#plotting accuracy over time
plt.figure(2)
plt.plot(history.history["accuracy"])
plt.plot(history.history["val_accuracy"])
plt.legend(["Training","Validation"])
plt.title("Accuracy")
plt.xlabel("Epoch")

plt.show()

#calculating the score of our model using test data
score = model.evaluate(img_test,cat_test,verbose=0)

#system update
print("The test score is equal to:",score[0])
print("Test accuracy is equal to:",score[1])

# #saving model
# stored_model = open("Trained models/model_trained.p","wb") #creating pickle to store model (wb = write bytes)
# pickle.dump(model,stored_model) #dumping data
# stored_model.close() #ending pickle commands
#using pickle package gives weakrf error

model.save("Trained models/trained_model.h5") #exporting model for later use

#TODO export csv containing cat_map

#end of code
print("Code has run successfully")