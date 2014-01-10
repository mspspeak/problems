




# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

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
		upperbound = n / i
		i += 1
	return return_value

primes = []
for x in xrange(2, 2000000):
	if is_prime(x):
		primes.append(x)

print sum(primes)

# $ python euler_ten.py 
# 142913828922
