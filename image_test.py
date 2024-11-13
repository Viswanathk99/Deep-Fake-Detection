from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Layer

# Define the custom layer
class CustomLayer(Layer):
    def __init__(self, **kwargs):
        super(CustomLayer, self).__init__(**kwargs)

    def call(self, inputs):
        return inputs * 2

# Path to your model file
model_path = 'path_to_your_model.h5'

# Define the custom objects
custom_objects = {'CustomLayer': CustomLayer}

# Load the model with custom objects
loaded_model = load_model(model_path, custom_objects=custom_objects)

# You can now use `loaded_model` in your code
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Layer

# Define the custom layer
class CustomLayer(Layer):
    def __init__(self, **kwargs):
        super(CustomLayer, self).__init__(**kwargs)

    def call(self, inputs):
        return inputs * 2

# Path to your model file
model_path = 'path_to_your_model.h5'

# Define the custom objects
custom_objects = {'CustomLayer': CustomLayer}

# Load the model with custom objects
loaded_model = load_model(model_path, custom_objects=custom_objects)

