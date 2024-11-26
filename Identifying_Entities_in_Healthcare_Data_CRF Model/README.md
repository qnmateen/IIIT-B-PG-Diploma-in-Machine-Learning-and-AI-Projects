# Named Entity Recognition for Medical Data {Conditional Random Fields (CRF)}

This project aims to build a custom Named Entity Recognition (NER) model using Conditional Random Fields (CRF) to identify diseases and their corresponding treatments from medical data. The dataset consists of medical notes and reviews, where diseases and treatments are not explicitly mentioned but can be inferred from the context.

## Dataset

The dataset is provided in the form of four files:

1. `train_sent`: Contains the training sentences, where each word is on a separate line, and sentences are separated by blank lines.
2. `train_label`: Contains the corresponding labels for each word in the training sentences, with labels 'O' (Other), 'D' (Disease), and 'T' (Treatment).
3. `test_sent`: Contains the test sentences, following the same format as `train_sent`.
4. `test_label`: Contains the corresponding labels for each word in the test sentences.


## Project Tasks

1. **Data Preprocessing**:
   - Construct proper sentences from individual words in the `train_sent` and `test_sent` files.
   - Construct sequences of labels from the `train_label` and `test_label` files.
   - Print five sample sentences along with their labels.
   - Print the count of sentences in the processed train and test datasets.
   - Print the count of lines of labels in the processed train and test datasets.

2. **Concept Identification**:
   - Use spaCy to extract tokens with NOUN or PROPN PoS tags from the entire dataset (train + test).
   - Find the frequency of these tokens and print the top 25 most common ones.

3. **Defining Features for CRF**:
   - Define features for the CRF model, including PoS tags and the preceding word.
   - Mark the beginning and end words of sentences as features.

4. **Getting Features and Labels**:
   - Write code to extract feature values for each sentence.
   - Write code to get the list of labels for each preprocessed label line.

5. **Defining Input and Target Variables**:
   - Extract feature values for each sentence as input variables for the CRF model.
   - Extract labels as target variables for the train and test datasets.

6. **Building the CRF Model**:
   - Build the CRF model using the defined features and target variables.

7. **Evaluation**:
   - Predict labels for each token in the test sentences.
   - Calculate the F1 score using the actual and predicted labels.

8. **Identifying Diseases and Treatments**:
   - Create a dictionary where diseases are keys and treatments are values.
   - Predict the treatment for the disease "hereditary retinoblastoma".

## Getting Started

1. Install the required dependencies (Python, spaCy, sklearn-crfsuite, etc.).
2. Download the dataset files (`train_sent`, `train_label`, `test_sent`, `test_label`).

## Assumptions

- If a disease is mentioned in a sentence, the treatment mentioned in the same sentence is assumed to be the treatment for that disease.
- The same treatment can work for different diseases.
