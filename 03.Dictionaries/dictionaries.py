# Dictionaries in Python are used to store data values in key:value pairs. A dictionary is a collection which is ordered, changeable and does not allow duplicates. The below code demonstrates how to create a dictionary, access its values, and modify it.

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer) # Will print the entire dictionary
print(customer.get("birthdate")) # None
print(customer.get("birthdate", "Jan 1, 1980")) # Will print "Jan 1, 1980" if birthdate is not found
customer["birthdate"] = "Jan 1, 1980" # Adding a new key-value pair to the dictionary
customer["name"] = "Jack Smith" # Updating the value of an existing key in the dictionary
print(customer["name"]) # Jack Smith
print(customer) # Will print the entire dictionary with the new key-value pair and updated name


# The below code demonstrates how to use a dictionary to map numbers to their corresponding words. It takes a phone number as input and outputs the corresponding words for each digit.

phone = input("Phone: ")
numbers_mapping = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

output = ""
for ch in phone:
    output += numbers_mapping.get(ch, "!") + " " 
print(output)