# Alzheimer's Disease Classification Model

## Overview

This repository contains a machine learning model for classifying Alzheimer's disease into four classes: Mild Demented, Very Mild Demented, Non-Demented, and Unknown Demented. The model has been trained with a test accuracy of 99.12%.

## Classes

- Mild Demented
- Very Mild Demented
- Non-Demented
- Unknown Demented

## Model Details

The model is based on a state-of-the-art neural network architecture and has been trained on a comprehensive dataset of Alzheimer's disease images. The training process achieved an impressive 99.12% accuracy on the test set, demonstrating its robustness in classifying different stages of Alzheimer's disease.

## Usage

To use the trained model for predicting Alzheimer's disease classes based on an input image, follow these steps:

1. **Ensure Dependencies are Installed:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Run Streamlit App:**
    ```bash
    streamlit run final.py
    ```

3. **Access the Provided URL:**
    Open the URL provided in your web browser.

4. **Upload an Image:**
    Upload an image in PNG, JPG, or JPEG format.

5. **Prediction:**
    The model will predict the Alzheimer's disease class of the given image.

### [Click here to access the hosted Streamlit app](https://dementiaclassification.streamlit.app/)

## Note

- The model's accuracy is based on the training dataset, and its performance on new, unseen data may vary.
- Ensure that the input images are clear and relevant to Alzheimer's disease diagnosis for accurate predictions.

## Contributing

Feel free to explore and contribute to the project. If you encounter any issues or have suggestions, please open an issue in the repository.

---

**Note:** Make sure to have Python and the required dependencies installed before running the code. Adjust file names and paths based on your actual project structure.
