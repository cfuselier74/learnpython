panagram = """The quick brown 
fox jumps\tover 
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807".split(",")
print(numbers)

numbers_ints = []
for number in numbers:
    numbers_ints.append(int(number))

print(numbers_ints)

input_text = "7,5,-1"
numbers = input_text.split(",")
print(numbers)
