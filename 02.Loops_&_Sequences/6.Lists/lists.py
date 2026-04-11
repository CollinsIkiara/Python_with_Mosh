# The below code demonstrates the use of lists in Python. It shows how to create a list and access its elements.

names = ['John', 'Edward', 'Lewis', 'Collins', 'Sarah', 'Joy', 'Rebecca']
print(names)
print(names[:])
print(names[0])
print(names[-1])
print(names[3])
print(names[2:])
print(names[2:6])

print("\n") # Printing a new line for better readability

# The following code finds the maximum number in the list of numbers. However, there is a mistake in the code.

numbers = [12, 34, 87, 56, 23, 45, 88, 90, 67]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)