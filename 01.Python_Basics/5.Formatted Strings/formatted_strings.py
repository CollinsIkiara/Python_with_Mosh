# The first method of formatting strings is to use the + operator to concatenate strings together. The second method is to use f-strings, which are a more concise and readable way to format strings.

first = 'John'
last = 'Doe'
message = first + ' [' + last + '] is a coder.'
print(message)
msg = f'{first} [{last}] is a coder.'
print(msg)