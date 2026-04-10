# This car game is a simple text-based game where the user can start and stop a car. The user can also ask for help or quit the game. It also checks if the car is already started or stopped before allowing the user to start or stop it again.

command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car stopped!")
    elif command == "help":
        print("""start - to start the car
stop - to stop the car
quit - to exit
""")
    elif command == "quit":
        break
    else:
        print("I don't understand that...")
