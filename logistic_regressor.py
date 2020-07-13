import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.utils import np_utils
from keras.utils.vis_utils import plot_model
import keras.utils

class LogisticRegressor():

    def __init__(self):

        self.input_size = 784 #28x28
        self.output_size = 10 #10 numbers    

    def load_model(self):
      
        self.model = keras.models.Sequential()
        self.model.add(keras.layers.Dense(self.output_size, input_dim=self.input_size, activation='softmax'))
        
    def run_model(self, train_images, train_labels):

        #reshape and normalize the data
        train_images = train_images.reshape(60000, self.input_size)  
        train_images = train_images.astype('float32')      
        train_images /= 255
        train_labels = np_utils.to_categorical(train_labels, self.output_size)

        epochs = 10
        batch_size = 128
  
        self.model.compile(optimizer=tf.keras.optimizers.Adagrad(learning_rate = 0.01), loss='categorical_crossentropy', metrics=['accuracy'])
        history = self.model.fit(train_images, train_labels,
                            batch_size=batch_size, epochs=epochs,
                            verbose=1)
        
    def predict_model(self, test_images):

        #reshape and normalize the data
        test_images = test_images.reshape(10000, self.input_size)
        test_images = test_images.astype('float32')
        test_images /= 255
        

        predictions = self.model.predict(test_images) 

        return predictions

def fit(images):
    regressor = LogisticRegressor()
    regressor.load_model()
    regressor.run_model(train_images=images[0], train_labels=images[1])

    return [regressor]

def predict(images, reg):

    regressor = reg[0]

    return regressor.predict_model(images)
    

(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()
reg = fit([train_images, train_labels])
predictions = predict(reg, test_images)
print(predictions)
print(test_labels)
