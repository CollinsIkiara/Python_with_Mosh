# This program demonstrates how to use the list method append() to create a list of unique numbers from a given list of numbers, i.e., it removes duplicates from the list.

numbers = [5, 6, 4, 3, 4, 5, 9, 5, 1, 2]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

## The following are examples of list methods that can be used to manipulate lists in Python:
# 1. append(): Adds an element to the end of the list.
# 2. insert(): Inserts an element at a specified position in the list.
# 3. remove(): Removes the first occurrence of a specified element from the list.
# 4. pop(): Removes and returns the element at a specified position in the list.
# 5. clear(): Removes all elements from the list.
# 6. index(): Returns the index of the first occurrence of a specified element in the list.
# 7. count(): Returns the number of occurrences of a specified element in the list.
# 8. sort(): Sorts the elements of the list in ascending order.
# 9. reverse(): Reverses the order of the elements in the list.
# 10. copy(): Returns a shallow copy of the list.
# 11. in operator: Checks if an element is present in the list and returns True or False.