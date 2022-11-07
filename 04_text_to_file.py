import re

# Data to be outputted
data = ['I', 'love', 'my ass', 'royally']

# Get filename cant be blank/invalid
# assume valid data for now

has_error = "yes"
while has_error == "yes":
    has_error = "no"
    filename = input("Enter a name for your file. It can be any name you wish")

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            problem = "(no space allowed)"
        else:
            problem = ("(no {}'s allowed)".format(letter))
        has_error = "yes"

    if filename == "":
        problem = "cant be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Filename is big wrong, you see {} is not right, big wrong, perhaps MASSIVE wrong".format(problem))
        print()
    else:
        print("You entered a valid filename finally. Massive right, not massive wrong,good job")


# add .txt suffix
filename = filename + ".txt"

# create file to hold data
f = open(filename, "w+")

# add new line at end of each item
for item in data:
    f.write(item + "\n")

# close file
f.close()
