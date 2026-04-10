# This program demonstrates the use of nested loops to create patterns based on lists of numbers.

numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ""
    for x in range(x_count):
        output += "x"
    print(output)
 
print("\n") # Print a new line to separate the two patterns
    
digits = [2, 2, 2, 2, 5]

for o_count in digits:
    result = ""
    for o in range(o_count):
        result += "o"
    print(result)