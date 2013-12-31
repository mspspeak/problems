
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divisible_by(a,b):
	if (a != 0) and (b != 0):
		return (a % b) == 0 
	else:
		return False

def get_lcm(a, b):
	min_number = min((a, b))
	max_number = max((a, b))

	upper_limit = a * b
	found_lcm = False
	lcm = None
	i = 1
	while i * max_number <= upper_limit and not found_lcm:
		if divisible_by(i * max_number, min_number):
			lcm = i * max_number
			found_lcm = True
		i+=1
	return lcm

print get_lcm(6, 9)


def get_lcm_of_list(number_list):
	if len(number_list) == 0:
		raise
	elif len(number_list) == 1:
		return number_list[0]
	else:
		value_a = number_list.pop(0)
		while number_list:
			value_b = number_list.pop(0)
			value_a = get_lcm(value_a, value_b)
	return value_a

print get_lcm_of_list(range(1,11))
print get_lcm_of_list(range(1,21))
