#
# strings are 0 index in python
parrot = "Norwegian Blue"

print(parrot[0:6]) # Norweg
print(parrot[3:5]) # we
print(parrot[0:9]) # Norwegian including start value
print(parrot[:9]) # Norwegian excluding start value Python will start at beginning of string

print(parrot[10:14]) # Blue includes stop number
print(parrot[10:]) # Blue excludes stop number, Python will go to end of string

print(parrot[:]) # prints value of parrot.