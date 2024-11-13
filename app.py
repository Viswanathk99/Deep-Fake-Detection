from image_test import loaded_model
import numpy as np
from tensorflow.keras.optimizers import Adam

# Compile the model manually (if you plan to train it)
loaded_model.compile(optimizer=Adam(), loss='mean_squared_error')

# Ensure the model is loaded
print("Model loaded successfully")

# Example input data for inference
input_data = np.random.random((1, 10))

# Make a prediction using the loaded model
prediction = loaded_model.predict(input_data)
print("Prediction:", prediction)

# Optionally, print the model summary
loaded_model.summary()
