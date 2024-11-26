# Melanoma Detection using Convolutional Neural Networks

This project aims to build a multiclass classification model using a custom convolutional neural network (CNN) in TensorFlow to accurately detect melanoma, a type of skin cancer. The model will be trained on a dataset consisting of 2357 images of malignant and benign oncological diseases, sourced from the International Skin Imaging Collaboration (ISIC).

## Dataset 

LINK - https://drive.google.com/file/d/1xLfSQUGDl8ezNNbUkpuHOYvSpTyxVhCs/view?usp=sharing

The dataset contains images of the following diseases:
- Actinic keratosis
- Basal cell carcinoma
- Dermatofibroma
- Melanoma
- Nevus
- Pigmented benign keratosis
- Seborrheic keratosis
- Squamous cell carcinoma
- Vascular lesion

The dataset is slightly imbalanced, with melanoma and mole images being slightly dominant.

## Project Pipeline

1. **Data Reading/Data Understanding**
   - Define the path for train and test images.

2. **Dataset Creation**
   - Create train and validation datasets from the train directory with a batch size of 32.
   - Resize images to 180x180 pixels.

3. **Dataset Visualization**
   - Visualize one instance of all nine classes present in the dataset.

4. **Model Building & Training (Initial)**
   - Create a custom CNN model to accurately detect the nine classes.
   - Rescale images to normalize pixel values between (0, 1).
   - Choose an appropriate optimizer and loss function for model training.
   - Train the model for ~20 epochs.
   - Evaluate the model for overfit or underfit.

5. **Data Augmentation**
   - Choose an appropriate data augmentation strategy to resolve underfitting/overfitting.

6. **Model Building & Training (Augmented Data)**
   - Create a CNN model with the augmented data.
   - Rescale images to normalize pixel values between (0, 1).
   - Choose an appropriate optimizer and loss function for model training.
   - Train the model for ~20 epochs.
   - Evaluate the model to see if the issues are resolved.

7. **Class Distribution**
   - Examine the current class distribution in the training dataset.
   - Identify the class with the least number of samples.
   - Identify the classes that dominate the data in terms of proportionate number of samples.

8. **Handling Class Imbalances**
   - Rectify class imbalances present in the training dataset using the Augmentor library.

9. **Model Building & Training (Rectified Class Imbalance Data)**
   - Create a CNN model with the rectified class imbalance data.
   - Rescale images to normalize pixel values between (0, 1).
   - Choose an appropriate optimizer and loss function for model training.
   - Train the model for ~30 epochs.
   - Evaluate the model to see if the issues are resolved.

