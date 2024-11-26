# Import routines

from sqlite3 import Time
import numpy as np
import math
import random
from itertools import permutations

# Defining hyperparameters
m = 5 # number of cities, ranges from 1 ..... m
t = 24 # number of hours, ranges from 0 .... t-1
d = 7  # number of days, ranges from 0 ... d-1
C = 5 # Per hour fuel and other costs
R = 9 # per hour revenue from a passenger


class CabDriver():

    ##visited
    def __init__(self):
        """initialise your state and define your action space and state space"""
        #since there are 5 i.e points there are 4 (n-1) drop locations that are possible hence total action space will in order n(n-1)
        self.action_space = [(0, 0)] + list(permutations([i for i in range(m)], 2))

        #there are 5 locations, 24 hours a day and 7 days a week. totally state would contain 5+24+7
        self.state_space = [(a, b, c) for a in range(1, m+1) 
                            for b in range(t) 
                            for c in range(d)]
        #pick the random start
        self.state_init = random.choice([(0,0,0), (1,0,0), (2,0,0), (3,0,0), (4,0,0)])
        # Start the first round
        self.reset()


    ## Encoding state (or state-action) for NN input

    def state_encod_arch1(self, state):
        """convert the state into a vector so that it can be fed to the NN. This method converts a given state into a vector format. Hint: The vector is of size m + t + d."""

        state_encod = [0 for _ in range(m+t+d)]
        state_encod[state[0]] = 1
        state_encod[m+state[1]] = 1
        state_encod[m+t+state[2]] = 1

        return state_encod

    ## Getting number of requests

    ##visited
    def requests(self, state):
        """Determining the number of requests basis the location. 
        Use the table specified in the MDP and complete for rest of the locations"""
        location = state[0]
        if location == 0:
            requests = np.random.poisson(2)
        if location == 1:
            requests = np.random.poisson(12)
        if location == 2:
            requests = np.random.poisson(4)
        if location == 3:
            requests = np.random.poisson(7)
        if location == 4:
            requests = np.random.poisson(8)        
        if requests >15:
            requests =15

        #get sample actions based on possion distribution
        possible_actions_index = random.sample(range(1, (m-1)*m +1), requests) # (0,0) is not considered as customer request
        
        #get action of all possible actions
        actions = [self.action_space[i] for i in possible_actions_index]
        ##append no action or leisure time
        if (0, 0) not in actions:
            actions.append((0,0))
            possible_actions_index.append(20)

        return possible_actions_index,actions   

    

    #visited
    def get_ride_time(self, state, action,Time_matrix):
        transit_time = 0    # to go from current  location to pickup location
        wait_time = 0
        ride_time = 0
        #state represents current location
        curr_loc = state[0]
        #get current time from state
        curr_time = state[1]
        #get current day from state
        curr_day = state[2]

        #in action tuple (pickup, drop)
        pickup_loc = action[0]
        drop_loc = action[1]

        """ 
        there are 3 cases to be handled
        1. Driver does pick any ride
        2. Driver is at pickup location
        3. Driver is not at the pickup point.
        """

        if ((pickup_loc== 0) and (drop_loc == 0)):
            # Handle case 1.0
            wait_time = 1
        elif (curr_loc == pickup_loc):
            # Handle case 2.0
            ride_time = Time_matrix[curr_loc][drop_loc][curr_time][curr_day]
        else:
            #Handle case 3.0
            transit_time = Time_matrix[curr_loc][pickup_loc][curr_time][curr_day]
            new_time, new_day = self.update_time_day(curr_time, curr_day, transit_time)
            # The driver is now at the pickup point
            # Time taken to drop the passenger
            ride_time = Time_matrix[pickup_loc][drop_loc][new_time][new_day]
        
        # Calculate total time as sum of all durations
        total_time = (wait_time + transit_time + ride_time)

        return wait_time,transit_time, ride_time, total_time

    #visited
    def reward_func(self, state, action, Time_matrix):
        """Takes in state, action and Time-matrix and returns the reward"""
        wait_time,transit_time,ride_time,_ = self.get_ride_time(state, action, Time_matrix)
        #get the passenger revenue time
        passenger_time = ride_time
        #get the idle time which is sum of wait time and transit time
        idle_time      = wait_time + transit_time
        #Compute the reward
        reward = (R * passenger_time) - (C * (passenger_time + idle_time))

        total_time=wait_time+transit_time+ride_time
        return reward, total_time

    def next_state_func(self, state, action, Time_matrix):
        """Takes state and action as input and returns next state"""
        """ 
        there are 3 cases to be handled
        1. Driver does pick any ride
        2. Driver is at pickup location
        3. Driver is not at the pickup point.
        """

        next_state = []

        #state represents current location
        curr_loc = state[0]
        #get current time from state
        curr_time = state[1]
        #get current day from state
        curr_day = state[2]

        #in action tuple (pickup, drop)
        pickup_loc = action[0]
        drop_loc = action[1]
        

        if ((pickup_loc== 0) and (drop_loc == 0)):
            # Refuse all requests, so wait time is 1 unit, next location is current location
            next_loc = curr_loc
        elif (curr_loc == pickup_loc):
            # next location is the drop location
            next_loc = drop_loc
        else:
            next_loc  = drop_loc

        _,_,_,total_time = self.get_ride_time(state, action, Time_matrix)
        next_time, next_day = self.update_time_day(curr_time, curr_day, total_time)

        # Construct next_state using the next_loc and the ne
        next_state = [next_loc, next_time, next_day]
        
        return next_state

    def step(self, state, action, Time_matrix):
        """
        Take a trip as cabby to get rewards next step and total time spent
        """
        # Get the next state and the various time durations
        next_state= self.next_state_func(state, action, Time_matrix)
        # Calculate the reward based on the different time durations
        rewards,total_time = self.reward_func(state, action, Time_matrix)
        
        return rewards, next_state, total_time       

    ##visited
    def reset(self):
        """
        Function to reset environment
        """
        return self.action_space, self.state_space, self.state_init



    ##visited
    def update_time_day(self, time, day, ride_duration):
        """
        This is the helper functin used to compute the day and hour change
        """
        ride_duration = int(ride_duration)
        #if trip gets completed within stipulated time go ahead
        if (time + ride_duration) < 24:
            time = time + ride_duration
        else:
            #if it spreads across day then adjust time by doing modulo
            time = (time + ride_duration) % 24 
            #update the day
            day = (day+1 ) % 7

        return time, day

 