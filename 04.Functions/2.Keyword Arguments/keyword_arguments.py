# The following code demonstrates the use of keyword arguments in Python functions. Keyword arguments allow us to specify the name of the parameter when calling a function, which can improve code readability and make it clear what each argument represents.

def greet_user(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")
    
print("Start")
greet_user("John", "Doe") # Positional arguments: the order matters
greet_user(last_name="Smith", first_name="Jane") # Keyword arguments: the order doesn't matter
greet_user("John", last_name="Smith") # Mixed arguments: positional first, then keyword
print("End")

# Important points:
# 1. For the most part, use positional arguments when passing arguments to a function. This is the most common way to call a function.
# 2. When using functions that take in multiple numerical values, and it may not be clear what those values represent, use keyword arguments to clarify the meaning of each value, for better code readability.
# 3. If we mix positional and keyword arguments in a function call, the positional arguments must come before the keyword arguments. Otherwise, Python will raise a SyntaxError.