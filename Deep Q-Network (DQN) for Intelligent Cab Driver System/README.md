# Cab Driver Profit Maximization using Deep Q-Learning

## Project Overview
This project implements a Deep Reinforcement Learning (DRL) solution for SuperCabs, helping cab drivers maximize their profits by making optimal ride selection decisions. The system uses Deep Q-Network (DQN) to learn the best strategies for accepting or rejecting ride requests based on various factors including location, time, and potential future opportunities.

## Business Problem
- Cab drivers face challenges in maximizing profits despite increasing revenues
- Rising electricity costs impact overall profitability
- Need for intelligent decision-making in ride selection
- Balance between immediate rewards and long-term profit potential

## Solution Approach
The project implements a Deep Q-Learning based system that:
- Assists drivers in selecting optimal ride requests
- Considers long-term profit implications
- Accounts for factors like:
  - Distance of ride
  - Pick-up location
  - Drop-off location potential
  - Time of day
  - Expected future ride probability

## Technical Implementation

### Environment Details
- State Space: Driver's location, current time, and ride requests
- Action Space: 
  - Accept one of the available rides
  - Go offline (reject all requests)
- Reward Structure: Based on profit earned from rides

### DQN Architecture
Two architecture options implemented:
1. Architecture 1: Direct state-action mapping
2. Architecture 2: Action-value function approximation


## Dependencies
- Python 3.x
- NumPy
- Pandas
- TensorFlow/PyTorch
- Matplotlib
- Jupyter Notebook


## Files Description
1. **Env.py**
   - Environment implementation
   - State management
   - Reward calculation
   - Request generation

2. **DQN_Agent_Arch[1/2].ipynb**
   - DQN implementation
   - Training loop
   - Hyperparameter configuration
   - Performance tracking

3. **TM.npy**
   - Time matrix data
   - Location-time relationships
   - Distance calculations

## Author
Qazi Noorul Mateen


## Acknowledgments
- Based on research paper: "Deep Reinforcement Learning for List-wise Recommendations"
