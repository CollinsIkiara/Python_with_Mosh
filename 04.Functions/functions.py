# This is a simple function that greets the user. It prints a greeting message to the console. The order matters as the message doesn't get printed until the function is called. The function is called between two print statements to show the flow of execution.

def greet_user():
    print("Hi there!")
    print("Welcome aboard")
    
print("Start")
greet_user()
print("Finish")