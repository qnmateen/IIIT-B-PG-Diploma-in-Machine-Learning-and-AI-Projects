# Automatic Ticket Classification System

## Project Overview
This project implements an automated system for classifying customer complaints in a financial institution using Natural Language Processing (NLP) and Machine Learning techniques. It automatically categorizes customer support tickets into relevant departments, enabling faster resolution and improved customer satisfaction.

## Problem Statement
For a financial company, customer complaints carry significant importance as they indicate shortcomings in products and services. Manual allocation of tickets to relevant departments becomes tedious as the company grows. This project aims to automate the classification of customer complaints based on products/services mentioned in the tickets.

## Dataset Link - https://drive.google.com/file/d/1Y4Yzh1uTLIBLnJq1_QvoosFx9giiR1_K/view
- Contains 78,313 customer complaints
- 22 features per complaint
- Format: JSON
- Unstructured text data requiring preprocessing

## Classification Categories
1. Credit card / Prepaid card
2. Bank account services
3. Theft/Dispute reporting
4. Mortgages/loans
5. Others

## Methodology

### 1. Text Preprocessing
- Data cleaning and normalization
- Stopword removal
- Tokenization
- Text vectorization

### 2. Topic Modeling
- Implemented Non-negative Matrix Factorization (NMF)
- Identified patterns and recurring words
- Generated topic clusters for complaint categories

### 3. Supervised Learning
Implemented multiple classification models:
- Logistic Regression
- Naive Bayes
- Decision Tree
- Random Forest

### 4. Model Evaluation
- Compared model performances
- Selected best performing model based on evaluation metrics
- Validated results on test data

## Implementation Steps

1. Data Loading
   - Converted JSON to DataFrame
   - Initial data exploration
   - Data cleaning

2. Exploratory Data Analysis (EDA)
   - Text analysis
   - Pattern identification
   - Feature distribution analysis

3. Feature Extraction
   - Text vectorization
   - Feature engineering
   - Dimensionality reduction

4. Topic Modeling
   - NMF implementation
   - Cluster analysis
   - Topic interpretation

5. Model Building
   - Data splitting
   - Model training
   - Hyperparameter tuning

6. Model Evaluation
   - Performance metrics calculation
   - Model comparison
   - Final model selection

## Dependencies
- Python 3.x
- NumPy
- Pandas
- Scikit-learn
- NLTK
- Matplotlib
- Seaborn
