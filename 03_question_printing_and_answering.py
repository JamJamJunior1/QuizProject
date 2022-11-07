valid = False
while not valid:
    try:
        name = (input("What is your name?"))
        valid = True
    except ValueError:
        print("Error please enter a name with letters")

valid = False
while not valid:
    try:
        age = int(input("What is your age?"))
        valid = True
    except ValueError:
        print("Error please enter a whole number")

valid = False
while not valid:
    try:
        favourite_animal = (input("What is your favourite animal?"))
        valid = True
    except ValueError:
        print("Error please enter a name with letters")

pi = 3.142
valid = False
while not valid:
    try:
        pi_guess = float(input("What is pi up to 3 decimal places?"))

        if pi == pi_guess:
            print('Correct')
        else:
            print("Sorry {:.3f} is incorrect {:.3} is the right answer".format(pi_guess,pi))
        valid = True
    except ValueError:
        print("Error please enter a number")

print("Great choice of well everything")
