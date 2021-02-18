# Dice Rolling Library, Ryan Kelley, February 18, 2021, 1:44PM 

import random 
import time

# d4 Simulator 
def roll_d4(num_roll): # num_roll is an ARGUMENT 
    rolls = 0
    the_sum = 0 

    while rolls < num_roll: 
        result = random.randint(1, 4)
        print(f"You have rolled a {result}.\n")
        time.sleep(1)
        rolls += 1 # Increments rolls by 1 each time. 
        the_sum += result 
    print(f"The total of the {num_roll} rolls was {sum}\n") # Use this line to print the sum. 

roll_d4(4) 
