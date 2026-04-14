## This code demonstrates the use of the random module in Python to generate random numbers and select random elements from a list. It also defines a Dice class that simulates rolling two six-sided dice.


# The below code demonstrates how to use the random module in Python to generate random numbers by using the .random() and .randint() functions. 

import random

for i in range(3): # Loop over 3 iterations
    print(random.random()) # Generate and print a random float between 0.0 and 1.0
    
for i in range(3):
    print(random.randint(1, 10)) # Generate and print a random integer between 1 and 10 (inclusive)
    

# The below code demonstrates how to randomly select a leader from a list of members using the random.choice() function.
    
members = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
leader = random.choice(members) # Randomly select a leader from the members list
print(leader)

# The following code defines a Dice class with a roll method that simulates rolling two six-sided dice and returns their values as a tuple.


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second
    
dice = Dice()
print(dice.roll())
