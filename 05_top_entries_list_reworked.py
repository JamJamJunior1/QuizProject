# Get data from user and store it in a list, showing te most recent entries first

# Set up empty list
all_answers = []

# Get five items of Data
get_item = ""
while get_item != "xxx":
    get_item = input("Enter an item: ")

    if get_item == "xxx":
        break

    all_answers.append(get_item)

print()

if len(all_answers) == 0:
    print("list big empty")

else:

    # Show that everything got to the list
    print()
    print("The Complete Edition")
    print(all_answers)

    # print items starting at the end of the list
    if len(all_answers) >= 3:
        print("Most Recent")
        for item in range(0, 3):
            print(all_answers[len(all_answers) - item - 1])

    else:
        print("Newest to Oldest")
        for item in all_answers:
            print(all_answers(len(all_answers) - all_answers.index()))
