letters = "abcdefghigklmnopqrstuvwxyz"
letters2 = ""
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters2[0])

#includes last index to start from end and go to beginning.
# No Stop value so it processes whole string
backwards = letters[25::-1]
print(backwards)

#includes no start or stop values.
# Python understands to start from end and process to beginning due to (-) step value
backwards2 = letters[::-1]
print(backwards2)

print()
print(letters[16:13:-1])

print()
print(letters[4::-1])

print()
print(letters[25:17:-1])
print(letters[:-9:-1])