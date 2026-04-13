# This is a reusable function that converts text-based emojis into their corresponding Unicode emojis.

def emoji_converter(message):
    words = message.split(" ") # Split the input message into individual words based on spaces.

    emojis = {
        ":)": "😊",
        ":(": "😞"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input(">") # Prompt the user to input a message that may contain text-based emojis.
print(emoji_converter(message)) # Takes the user's input message as an argument for the emoji_converter function and prints the converted message with Unicode emojis.
