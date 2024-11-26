# Telecom Churn Prediction

This project aims to predict customer churn in the telecom industry and identify the main indicators of churn. By analyzing customer-level data of a leading telecom firm, we will build predictive models to identify high-value customers at high risk of churn and provide recommendations to manage customer churn.

## Problem Statement

In the highly competitive telecom industry, customer retention is crucial. The goal of this project is to predict customer churn, specifically for high-value customers, and identify the key indicators of churn. By doing so, the telecom company can take proactive measures to retain customers and minimize revenue loss.

## Data

The dataset contains customer-level information for a span of four consecutive months - June, July, August, and September. The data includes various features such as customer demographics, usage patterns, and revenue information.
### Link to Data - https://drive.google.com/file/d/1SWnADIda31mVFevFcfkGtcgBHTKKI94J/view

## Methodology

1. Data Preparation:
   - Derive new features based on business understanding.
   - Filter high-value customers based on the 70th percentile of the average recharge amount in the first two months.
   - Tag churners based on the fourth month's usage criteria.
   - Remove attributes corresponding to the churn phase.

2. Exploratory Data Analysis:
   - Conduct exploratory analysis to gain insights into customer behavior and churn indicators.
   - Visualize relevant patterns and relationships in the data.

3. Feature Engineering:
   - Create new features that capture relevant information for churn prediction.
   - Handle missing values and convert columns to appropriate formats.

4. Dimensionality Reduction:
   - Apply Principal Component Analysis (PCA) to reduce the number of variables.

5. Model Building:
   - Train various classification models to predict churn.
   - Handle class imbalance using appropriate techniques.
   - Tune model hyperparameters to optimize performance.

6. Model Evaluation:
   - Evaluate the models using relevant evaluation metrics, focusing on accurately identifying churners.
   - Select the best-performing model based on the chosen evaluation metric.

7. Feature Importance:
   - Build a separate model (e.g., logistic regression or tree-based model) to identify important predictor attributes.
   - Handle multi-collinearity in the case of logistic regression.
   - Visualize the importance of features using plots or summary tables.

8. Recommendations:
   - Provide strategies to manage customer churn based on the insights gained from the analysis and modeling.
