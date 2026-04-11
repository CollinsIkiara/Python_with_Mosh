# 2D lists (lists of lists) in Python. The following code demonstrates how to create a 2D list (matrix), modify an element, and iterate through the elements.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][1] = 20
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)