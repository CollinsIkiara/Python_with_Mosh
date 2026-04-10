# This is a simple guessing game where the user has to guess a secret number within a certain number of attempts, implemented using a while loop.

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You win!")
        break # Exit the loop if the user guesses correctly
else: # This else block executes if the loop completes without a break (i.e., the user fails to guess the number within the limit)
    print("Sorry, you failed.")