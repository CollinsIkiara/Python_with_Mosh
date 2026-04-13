# The following code is a simple emoji converter that takes user input and replaces certain text representations of emotions with their corresponding emojis by using a dictionary to map the text to emojis. The user is prompted to enter a message, which is then split into words. Each word is checked against the dictionary, and if it matches, it is replaced with the corresponding emoji. Finally, the converted message is printed out.

message = input(">")
words = message.split(" ")

emojis = {
    ":)": "😊",
    ":(": "😞"
}

output = ""
for word in words:
   output += emojis.get(word, word) + " " 
print(output)