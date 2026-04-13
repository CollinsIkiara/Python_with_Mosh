# Exceptions are errors that occur during the execution of a program. They can be handled using try-except blocks.

try:
    age = int(input("Age: ")) # Converts the input to an integer. If the input is not a valid integer, it raises a ValueError.
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError: # Raises a ZeroDivisionError if the age is zero, as division by zero is not allowed.
    print("Age cannot be zero")
except ValueError: # Raises a ValueError if the input is not a valid integer.
    print("Invalid value")