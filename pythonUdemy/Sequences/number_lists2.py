empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = sorted("432985617")
digits2 = list("432985617")
print(digits)
print(digits2)

more_numbers = list(numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)

more_numbers2 = numbers[3:]
print(more_numbers2)

more_numbers3 = numbers.copy()
print(more_numbers3)