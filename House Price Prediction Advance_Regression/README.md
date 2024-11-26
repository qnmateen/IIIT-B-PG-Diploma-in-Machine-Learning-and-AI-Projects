# Surprise Housing - House Price Prediction

This project aims to build a regression model using regularization techniques to predict the actual value of prospective properties for Surprise Housing, a US-based housing company entering the Australian market. The company uses data analytics to purchase houses at a price below their actual values and flip them on at a higher price.

## Problem Statement

Surprise Housing wants to enter the Australian market by purchasing prospective properties and flipping them at a higher price. To make informed decisions, they need a regression model that can predict the actual value of the properties based on various variables. The company wants to know:

- Which variables are significant in predicting the price of a house.
- How well those variables describe the price of a house.

Additionally, the project aims to determine the optimal value of lambda for ridge and lasso regression.

## Business Goal

The goal is to model the price of houses with the available independent variables. This model will help the management understand how exactly the prices vary with the variables. They can accordingly manipulate the strategy of the firm and concentrate on areas that will yield high returns. Further, the model will be a good way for management to understand the pricing dynamics of a new market.

## Data

The dataset used for this project contains information about the sale of houses in Australia. It is provided in a CSV file format.

## Methodology

1. Data Exploration and Preprocessing:
   - Load and examine the dataset.
   - Handle missing values and outliers.
   - Perform feature scaling if necessary.

2. Feature Selection:
   - Identify the significant variables that impact house prices.
   - Use techniques like correlation analysis and feature importance to select relevant features.

3. Model Building:
   - Split the data into training and testing sets.
   - Implement regularization techniques: Ridge Regression and Lasso Regression.
   - Train the models on the training data.

4. Model Evaluation:
   - Evaluate the performance of the models using appropriate metrics (e.g., Mean Squared Error, R-squared).
   - Determine the optimal value of lambda for ridge and lasso regression using techniques like cross-validation.

5. Model Interpretation:
   - Analyze the coefficients of the selected variables to understand their impact on house prices.
   - Provide insights and recommendations based on the model results.



## Usage

1. Clone the repository.
2. Install the required libraries.
