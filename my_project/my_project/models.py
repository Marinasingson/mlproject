import tensorflow as tf
import numpy as np

def predict_digit(image):
    # Load the saved model
    model = tf.keras.models.load_model('model.h5')

    # Preprocess the image
    img = image.convert('L')
    img = img.resize((28, 28))
    img = np.array(img)
    img = img.reshape((1, 28, 28, 1))
    img = img / 255.0

    # Make the prediction
    prediction = model.predict_classes(img)[0]

    return prediction
