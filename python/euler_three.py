

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?



# Start at 2 and look for divisors and then ask if those are prime



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

def find_largest_prime_divisor(n):
	i = 2
	upperbound = n
	largest_d = 1
	while i < upperbound:
		if divisible_by(n, i):
			value = n / i
			if i < value:
				if is_prime(i):
					largest_d = i
			else:
				if is_prime(value):
					largest_d = value
			upperbound = value

		i += 1
	return largest_d

def find_prime_divisors(n):
	i = 2
	upperbound = n
	while i < upperbound:
		if divisible_by(n, i):
			value = n / i
			if is_prime(i):
				yield i
			if is_prime(value):
				yield value
			upperbound = value
		i += 1


for i in xrange(100):
	print i, is_prime(i)

print is_prime(6857)

print find_largest_prime_divisor(600851475143)
print list(find_prime_divisors(600851475143))
print 71 * 839 * 1471 * 6857




