import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

# store data
# with open(filename, 'w+') as f:
#     json.dump(numbers, f)

# open data
with open(filename) as f:
    numbers = json.load(f)

print(numbers)