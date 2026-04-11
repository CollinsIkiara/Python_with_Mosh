# Unpacking is a powerful feature in Python that allows you to assign values from a collection (like a list or tuple) to multiple variables in a single line of code. This can make your code cleaner and more readable.

coordinates = (1, 2, 3) # A tuple containing three values. We can unpack it into three variables.
x, y, z = coordinates
print(x, y, z)

prices = [10, 20, 30] # A list containing three values. We can unpack it into three variables.
a, b, c = prices
print(a, b, c)