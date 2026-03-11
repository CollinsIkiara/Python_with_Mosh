# Day 2: 30 Days of python programming

# Declaring different types of variables
first_name = 'Collins'
last_name = 'Ikiara'
full_name = 'Collins Ikiara'
country = 'Kenya'
city = 'Nairobi'
age = 889
year = 2026
is_married = True
skills = ['Python', 'FastAPI']
is_true = True
is_light_on = False

# Declaring multiple variables in one line
full_name, country, city, age, year, skills = 'Collins Ikiara', 'Kenya', 'Nairobi', 889, 2026, ['Python', 'FastAPI']

# Checking the data types of the variables using the type() built-in function
print(type(first_name))  # str
print(type(last_name))   # str
print(type(full_name))   # str
print(type(country))     # str
print(type(city))        # str
print(type(age))         # int
print(type(year))        # int
print(type(is_married))  # bool
print(type(skills))      # list
print(type(is_true))     # bool
print(type(is_light_on)) # bool

# Finding the length of a string variable using the len() built-in function
print(len(first_name))  # 7

# Compare the length of first_name and last_name
print(len(first_name) == len(last_name))  # False

# Arithmetic operations
num_one = 5
num_two = 4

total = num_one + num_two
print(total)  # 9
diff = num_one - num_two
print(diff)  # 1
product = num_two * num_one
print(product)  # 20
division = num_one / num_two
print(division)  # 1.25
remainder = num_two % num_one
print(remainder)  # 4
exp = num_one ** num_two
print(exp)  # 625
floor_division = num_one // num_two
print(floor_division)  # 1

# Area and circumference of a circle
radius = 30

area_of_circle = 3.14 * radius ** 2
print(area_of_circle)  # 2826.0
circum_of_circle = 3.14 * radius * 2
print(circum_of_circle)  # 188.4
input_radius = int(input('Enter radius of a circle: '))
area_of_circle = 3.14 * input_radius ** 2
print(area_of_circle)

# Use the built-in input function to get input from the user and store them in variables.
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: '  )
country = input('Enter your country: ')
age = int(input('Enter your age: '))

help('keywords')  # List of reserved keywords in Python