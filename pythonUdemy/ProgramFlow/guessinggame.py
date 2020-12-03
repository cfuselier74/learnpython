import random

highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing

print("Please guess number between 1 and {} ".format(highest))
guess = 0

while guess != answer:
    guess = int(input())

    if guess == 0:
        break

    if guess == answer:
        print("You guessed the correct number")
        break
    else:
        if guess < answer:
            print("Please guess higher or 0 to quit")
        else:
            print("Please guess lower or 0 to quit")

# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed correctly")
#     else:
#         print("Sorry, You have not guessed correctly")