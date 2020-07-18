
import numpy as np
import keras
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from keras.preprocessing import image
#import h5py

def output(path,model,inverted_classes ):


    Y=[]
    img = image.load_img(path= path,target_size=(128,128,3))
    img = image.img_to_array(img)
    test_img = img.reshape((1,128,128,3))
    img_class = np.argmax(model.predict(test_img), axis=-1)#model.predict_classes(test_img)
    prediction = img_class[0]
    Y.append(prediction)
    prediction_classes = [ inverted_classes.get(item,item) for item in Y ]
    return str(prediction_classes[0])
def get_bot_pattern_type(path,inverted_classes):
    model = load_model(r'bot_pattern_type.h5')
    model.build()
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy','accuracy'])
    bot_pattern_type=output(path, model, inverted_classes)
    return str(bot_pattern_type)
def get_bot_sleeve_length(path,inverted_classes):
    model = load_model(r'bot_Sleeve_Length.h5')
    model.build()
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy','accuracy'])
    bot_Sleeve_length=output(path, model, inverted_classes)
    return str(bot_Sleeve_length)

def get_bot_multicolor_type(path,inverted_classes):
    model = load_model(r'bot_multicolor.h5')
    model.build()
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy','accuracy'])
    item_type=output(path, model, inverted_classes)
    return str(item_type)

def get_bot_item_type(path,inverted_classes):
    model = load_model(r'bot_Item.h5')
    model.build()
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy','accuracy'])
    item_type=output(path, model, inverted_classes)
    return str(item_type)
def get_up_item_type(path,inverted_classes):
    model = load_model(r'up_Item.h5')
    model.build()
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy','accuracy'])
    item_type=output(path, model, inverted_classes)
    return str(item_type)
def get_up_multicolor_type(path,inverted_classes):
    model = load_model(r'up_multicolor.h5')
    model.build()
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy','accuracy'])
    item_type=output(path, model, inverted_classes)
    return str(item_type)

def get_up_pattern_type(path,inverted_classes):
    model = load_model(r'top_pattern_type.h5')
    model.build()
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy','accuracy'])
    item_type=output(path, model, inverted_classes)
    return str(item_type)

def get_up_sleeve_length(path,inverted_classes):
    model = load_model(r'top_sleevelen_hist.h5')
    model.build()
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy','accuracy'])
    item_type=output(path, model, inverted_classes)
    return str(item_type)

def get_wear_type(path,inverted_classes):
    model = load_model(r'wear_type_hist.h5')
    model.build()
    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['categorical_accuracy','accuracy'])
    item_type=output(path, model, inverted_classes)
    return str(item_type)
