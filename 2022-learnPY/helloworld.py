print("Hello World!")
"""Convert text to ASCII binary"""
# Ask the user for text to convert
text = input("Enter text to convert: ")
# Convert text to ASCII binary
binary = ""
for character in text:
    binary += bin(ord(character))[2:].zfill(8) + " "
# Print the result 
print("The binary value of '" + text + "' is: " + binary)
# Append the binary value and text to a file
with open("binary.txt", "a") as file:
    file.write(binary + "\n")
    file.write(text + "\n")
    file.write("\n")
# Print a message to the user
print("\nThe binary value of '" + text + "' has been appended to binary.txt")

"""(Ignore) This part is hilarious"""
# Translate the text to french
# Ask the user for text to translate
text = input("Enter text to translate: ")
# Translate text to french
french = ""
for character in text:
    if character.lower() in "aeiouy":
        french += character + " "
    else:
        french += character + "o" + character + " "
# Print the result 
print("The french translation of '" + text + "' is: " + french)