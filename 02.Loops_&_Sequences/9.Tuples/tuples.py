# Tuples are immutable sequences. They are defined by enclosing the elements in parentheses (). You cannot modify a tuple after it has been created, which means you cannot add, remove, or change elements in a tuple. However, you can only get information about the elements as shown below.

numbers = (1, 2, 3, 4, 5)

print(numbers.count(3))
print(numbers.index(3))
print(numbers[0])