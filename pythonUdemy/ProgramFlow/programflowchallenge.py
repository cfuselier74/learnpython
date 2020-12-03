choice = 99
valid_option = [1, 2, 3, 4, 5, 0]

while choice != 0:
    print("You have selected {}.".format(choice))
    print("Please select an option: ")
    if choice not in valid_option:
        print("1.\tLearn Python")
        print("2.\tLearn Java")
        print("3.\tGo Swimming")
        print("4.\tLearn Python")
        print("5.\tGo to Bed.")
        print("0.\tExit")
    choice = int(input())
else:
    print("You have selected to exit the program")
