# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def square(value):
	return value * value

def square_list(list):
	return (square(x) for x in list)

sum_of_squares_to_10 = sum(square_list(range(1,11)))

square_of_sums_to_10 = square(sum(range(1,11)))

print square_of_sums_to_10 - sum_of_squares_to_10


sum_of_squares_to_100 = sum(square_list(range(1,101)))

square_of_sums_to_100 = square(sum(range(1,101)))

print square_of_sums_to_100, "-", sum_of_squares_to_100, "=", square_of_sums_to_100 - sum_of_squares_to_100