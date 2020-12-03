age = int(input("Please enter your age: "))
name = input("Please enter your name: ")

if 18 <= age <= 30:
    print("Welcome {}, to our special holiday".format(name))
else:
    print("Unfortunately {}, you do not qualify for our 18-30 holdiday".format(name))
