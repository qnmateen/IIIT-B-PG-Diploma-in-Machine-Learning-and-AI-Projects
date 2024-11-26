# Numerical Tic-Tac-Toe Reinforcement Learning Agent

## Project Overview
This project implements a Reinforcement Learning (RL) agent that learns to play Numerical Tic-Tac-Toe using Q-Learning. The agent plays with odd numbers against an environment that plays with even numbers, aiming to create a sum of 15 in any row, column, or diagonal.

## Game Rules
- Played on a 3x3 grid using numbers 1-9
- Each number can be used exactly once
- Two players:
  - RL Agent: Uses odd numbers {1, 3, 5, 7, 9}
  - Environment: Uses even numbers {2, 4, 6, 8}
- Agent (odd numbers) always moves first
- Goal: Make 15 points in a row, column, or diagonal
- Players can use opponent's numbers to make 15

## Project Structure
```
Reinforement Learning- TicTacToe/
│
├── TCGame_Env.py           # Environment implementation
├── TicTacToe_Agent.ipynb  # Agent implementation and training
├── q_values.pkl           # Saved Q-values
└── README.md
```

## Implementation Details

### MDP Framework
1. **State Space**
   - 3x3 grid representation
   - Each cell can be empty or contain numbers 1-9

2. **Action Space**
   - Available odd numbers for each state
   - Dynamic based on remaining unused numbers

3. **Reward Structure**
   - Win (Agent makes 15): +10
   - Loss (Environment makes 15): -10
   - Draw: 0
   - Each move: -1

4. **Terminal States**
   - Win (sum of 15 achieved)
   - Loss (environment achieves sum of 15)
   - Draw (board filled without sum of 15)

### Q-Learning Implementation
- State-action value function approximation
- Epsilon-greedy exploration strategy
- Experience replay for improved learning
- Hyperparameter tuning for optimal performance


## Files Description
1. **TCGame_Env.py**
   - Environment implementation
   - State management
   - Game rules and mechanics

2. **TicTacToe_Agent.ipynb**
   - Q-Learning implementation
   - Training process
   - Performance analysis
   - Convergence plots

## Author
Qazi Noorul Mateen
