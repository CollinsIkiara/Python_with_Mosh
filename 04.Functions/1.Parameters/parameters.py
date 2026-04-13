# The below code illustrates the use of parameters in a function. Parameters are placeholders for values that will be passed to the function when it is called. In this example, the function `greet_user` takes two parameters: `first_name` and `last_name`. When the function is called, we provide the actual values (also known as arguments) "John" and "Smith" for these parameters, which allows the function to greet the user by their full name.

def greet_user(first_name, last_name): # Parameters are defined in the function definition
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")
    
print("Start")
greet_user("John", "Smith") # Arguments: actual values passed to the function when it is called
print("Finish")