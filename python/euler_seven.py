

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?



def divisible_by(a,b):
	if (a != 0) and (b != 0):
		return (a % b) == 0 
	else:
		return False

def is_prime(n):
	i = 2
	upperbound = n
	return_value = True
	while i < upperbound and return_value:
		if divisible_by(n, i):
			return_value = False
		i += 1
	return return_value


count = 1
current_candidate = 2
while count < 10002:
	if is_prime(current_candidate):
		print count, ":", current_candidate
		count += 1
	current_candidate += 1



