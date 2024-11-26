# Gesture Recognition - Using CNN+RNN and Conv3D

This project aims to develop a cool feature in smart TVs that can recognize five different gestures performed by the user to control the TV without using a remote. The gestures are continuously monitored by the webcam mounted on the TV, and each gesture corresponds to a specific command:

- Thumbs up: Increase the volume
- Thumbs down: Decrease the volume
- Left swipe: 'Jump' backwards 10 seconds
- Right swipe: 'Jump' forward 10 seconds
- Stop: Pause the movie

## Dataset

The training data consists of a few hundred videos categorized into five classes. Each video (typically 2-3 seconds long) is divided into a sequence of 30 frames (images). The videos have been recorded by various people performing one of the five gestures in front of a webcam, similar to what the smart TV will use.

### Dataset link - https://drive.google.com/uc?id=1ehyrYBQ5rbQQe6yL4XbLWe3FMvuVUGiL

The data is organized in the following structure:
- `train` folder: Contains training videos and a CSV file with video details.
- `val` folder: Contains validation videos and a CSV file with video details.
- `test` folder: Contains test videos for model evaluation (withheld for evaluation purposes).

Each CSV file contains three main pieces of information for each video:
- Subfolder name: The name of the subfolder containing the 30 images of the video.
- Gesture name: The name of the gesture performed in the video.
- Numeric label: The numeric label (between 0-4) of the video.

The videos have two types of dimensions, either 360x360 or 120x160, depending on the webcam used to record them.

## Project Goals

The main goals of this project are:

1. **Generator**: Develop a data generator that can take a batch of videos as input without any error. Implement preprocessing steps like cropping, resizing, and normalization.

2. **Model**: Build a model that is able to train without any errors. The model should be optimized for minimal number of parameters (to reduce inference time) and high accuracy. Experiment with different architectures and hyperparameters to arrive at the best model.

3. **Write-up**: Create a detailed write-up that explains the procedure followed in choosing the final model. Start with the reason for choosing the base model, and then highlight the reasons and metrics taken into consideration to modify and experiment to arrive at the final model.

## Model Architectures

Two types of architectures are commonly used for analyzing videos:

1. **CNN + RNN**: Pass the images of a video through a CNN to extract features, then pass the sequence of features through an RNN to analyze the temporal information.

2. **3D Convolutional Network (Conv3D)**: Use 3D convolutions to process the video data, where the convolution operation is performed in both spatial and temporal dimensions.

In this project, you will experiment with both architectures and compare their performance.

## Getting Started

1. Download the dataset and unzip it to your working directory.
2. Install the required dependencies (tensorflow, keras, numpy, etc.).
3. Preprocess the data using the data generator.
4. Train the model using the fit_generator method.
5. Evaluate the model on the validation set and tune hyperparameters if necessary.
6. Test the final model on the test set and report the accuracy.

