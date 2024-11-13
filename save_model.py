from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Layer

# Define a custom layer
class CustomLayer(Layer):
    def __init__(self, **kwargs):
        super(CustomLayer, self).__init__(**kwargs)

    def call(self, inputs):
        return inputs * 2

# Build a simple model with the custom layer
inputs = Input(shape=(10,))
x = CustomLayer()(inputs)
outputs = Dense(1)(x)
model = Model(inputs, outputs)

# Save the model
model_path = 'path_to_your_model.h5'
model.save(model_path)
