# data = [104, 101, 4, 105, 308, 103, 5,
#         107, 100, 306, 106, 102, 108]
data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
        160, 170, 183, 185, 187, 199, 191, 350, 360]
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 199, 191]
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 199, 191, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 199, 191]
# data = [1041, 1051, 1101, 1201, 1301, 1301, 1501,
#         1601, 1701, 1831, 1851, 1871, 1881, 1911]
# data = []

min_valid = 100
max_valid = 200

# for i in range(len(data) - 1, -1, -1):
#     if (data[i] < min_valid) or (data[i] > max_valid):
#         del data[i]
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if (value < min_valid) or (value > max_valid):
        del data[top_index - index]

print(data)
