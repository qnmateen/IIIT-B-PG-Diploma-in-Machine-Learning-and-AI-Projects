# Bike Sharing Demand Prediction

This project aims to build a multiple linear regression model to predict the demand for shared bikes based on various factors. The project is based on a case study of a US bike-sharing provider, BoomBikes, which has suffered considerable dips in revenue due to the ongoing Corona pandemic. The company wants to understand the factors affecting the demand for shared bikes in the American market to prepare themselves for the post-quarantine situation and make huge profits.

## Problem Statement

BoomBikes, a US bike-sharing provider, has recently suffered considerable dips in their revenues due to the ongoing Corona pandemic. They have contracted a consulting company to understand the factors on which the demand for these shared bikes depends. Specifically, they want to understand the factors affecting the demand for these shared bikes in the American market. The company wants to know:

- Which variables are significant in predicting the demand for shared bikes.
- How well those variables describe the bike demands.

Based on various meteorological surveys and people's styles, the service provider firm has gathered a large dataset on daily bike demands across the American market based on some factors.

## Business Goal

The goal is to model the demand for shared bikes with the available independent variables. It will be used by the management to understand how exactly the demands vary with different features. They can accordingly manipulate the business strategy to meet the demand levels and meet the customer's expectations. Further, the model will be a good way for management to understand the demand dynamics of a new market.

## Data Preparation

The dataset contains variables like 'weathersit' and 'season' that have numeric values associated with specific labels. These numeric values should be converted into categorical string values before proceeding with model building. The 'yr' column, indicating the years 2018 and 2019, should be considered as a potential value-add to the model despite having only two values.

## Model Building

The dataset contains three columns named 'casual', 'registered', and 'cnt'. The 'cnt' variable, which indicates the total number of bike rentals including both casual and registered, should be used as the target variable for building the model.
