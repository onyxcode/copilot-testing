# find the number with the highest value
def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# make a list of random numbers
import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))

# use find_max to find the highest number in numbers
print(find_max(numbers))