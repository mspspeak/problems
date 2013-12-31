


# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def divisible_by(a,b):
	if (a != 0) and (b != 0):
		return (a % b) == 0 
	else:
		return False

def find_three_fives_less_than(n):
	i=0
	while i < n:
		if (divisible_by(i, 3) or divisible_by(i,5)): 
			yield i
		i+=1 

print sum(find_three_fives_less_than(1000))



