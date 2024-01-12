import streamlit as st
import tensorflow as tf
import numpy as np
import requests
from PIL import Image
import io
import pymongo

# Load the pre-trained model
model_path = "C:\\Users\\akash boss\\Alzheimer's Dementia Classification\\Alzheimer_CNN2d.h5"  # Replace with the actual path to your saved model
model = tf.keras.models.load_model(model_path)

# Define class labels
class_labels = ['Mild_Demented', 'Moderate_Demented', 'Non_Demented', 'Very_Mild_Demented']

# Set page title
st.set_page_config(
    page_title="Alzheimer's Detection",
    page_icon="✅",
    layout="centered",
    initial_sidebar_state="auto",
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select a page", ["Home", "Prediction"])

# MongoDB connection details
mongo_host = "mongodb://localhost:27017"
mongo_db = "Alzheimer" 
mongo_port = 27017

# Initialize MongoDB client
client = pymongo.MongoClient(mongo_host)

# Create a function to insert the prediction into MongoDB
def store_prediction(image_filename, predicted_class):
    db = client[mongo_db]
    
    # Create a collection (a table in MongoDB) for predictions if it doesn't exist
    prediction_collection = db.get_collection("predictions")

    # Define the data to be inserted
    data = {
        "image_filename": image_filename,
        "predicted_class": predicted_class,
    }

    # Insert the data into the collection
    prediction_collection.insert_one(data)

# Home page content with background image in the content
if page == "Home":
    st.title("Alzheimer's Disease Detection")
    st.write("This is the home page. Learn more about Alzheimer's disease here.")

    # Display background image within the content
    background_url = 'https://news.mit.edu/sites/default/files/images/202309/MIT-AlzGenome-01-press.jpg'
    background_image = Image.open(requests.get(background_url, stream=True).raw)
    st.image(background_image, use_column_width=True, caption="Alzheimer's Disease")

    # Add content about Alzheimer's disease
    st.write("Alzheimer's disease is a progressive neurodegenerative disorder that affects memory, thinking, and behavior.")

# Prediction page content without background image
if page == "Prediction":
    st.title("Alzheimer's Disease Detection")
    st.write("Upload an MRI brain image to predict Alzheimer's class.")

    # Image upload
    uploaded_image = st.file_uploader("Upload an MRI image", type=["jpg", "jpeg", "png"])

    # Prediction
    if uploaded_image is not None:
        st.write("Image Preview:")
        st.image(uploaded_image, use_column_width=True)

        image = Image.open(uploaded_image)
        image = np.array(image)

        # Check the number of dimensions in the image
        if len(image.shape) == 2:
            # Grayscale image with 1 channel
            # Convert it to RGB format by duplicating the channel
            image = np.stack((image,) * 3, axis=-1)

        # Resize the image to match model input size
        image = tf.image.resize(image, (128, 128))

        # Convert the image to float32
        image = tf.image.convert_image_dtype(image, tf.float32)

        # Add a batch dimension
        image = tf.expand_dims(image, axis=0)

        # Make predictions
        predictions = model.predict(image)
        predicted_label = class_labels[np.argmax(predictions)]

        st.write("Predicted Class:", predicted_label)

        # Store the prediction in MongoDB
        store_prediction(uploaded_image.name, predicted_label)
        st.write("Prediction stored in MongoDB.")

# Close the MongoDB connection when the Streamlit app is closed
st.text("End of the mongodb")
client.close()
