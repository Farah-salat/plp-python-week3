# BUG: The closing quotation mark was missing, causing a SyntaxError.
print("Welcome to the Bug Hunt!")
name = input("What is your name? ")
# BUG: The user's name was written as plain text and misspelled; I changed it to the name variable.
print(f"Nice to meet you, {name}")
# BUG: input() returned age as a string, so I converted it to an integer before adding 1.
age = int(input("How old are you? "))
# BUG: I converted the age calculation to a string so it can be combined with the message.
print("Next year you will be " + str(age + 1))
