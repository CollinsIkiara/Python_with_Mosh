# This function takes a number as input and returns its square.

def square(number):
    return number * number

print(square(3))  # Output: 9


# The below function does not have a return statement, so it will return None by default.

def sq(x):
    print(x * x)
    
print(sq(3))  # Output: 9 followed by None