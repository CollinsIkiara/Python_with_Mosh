# This code demonstrates the use of comparison operators (<, >, <=, >=, ==, !=) to validate the length of a name and based on that, print an appropriate message.

name = "Collins Ikiara"

if len(name) < 3:
    print("Name must be at least 3 characters long.")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters long.")
else:
    print("Name looks good!")