


# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


#a + b + c = 1000

#a * a + b * b - c * c = 0


# c = 1000 - a - b

# a * a + b * b  = (1000 - a - b) * (1000 - a - b)

# a * a + b * b = 1000 * 1000 - 1000 * a - 1000 * b - 1000 * a + a * a + a * b - 1000 * b + a * b + b * b

# a * a + b * b = 1000000 - 2000 * b - 2000 * b + a * a + 2 * a * b + b * b 

# 0 = 1000000 - 2000 * b - 2000 * a + 2 * a * b

# 0 = 500000 - 1000 * b - 1000 * a + a * b

# 1000 * b + 1000 * a - a * b = 500000

for a in range(1,1000):
	for b in range(1,1000):
		if (1000 * b) + (1000 * a) - (a * b) == 500000:
			print a, b, 1000 - a - b




