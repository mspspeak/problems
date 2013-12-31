

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def get_digits(integer):
	return list(str(integer))


print get_digits(123414)


def is_palindrome(list):
	if len(list) == 0:
		return True
	if len(list) == 1:
		return True
	else:	
		first = list.pop(0)
		last = list.pop()
		if first == last:
			return is_palindrome(list)
		else:
			return False

print is_palindrome(get_digits(123124124))
print is_palindrome(get_digits(1))
print is_palindrome(get_digits(22))
print is_palindrome(get_digits(123321))
print is_palindrome(get_digits(12321))


def divisible_by(a,b):
	if (a != 0) and (b != 0):
		return (a % b) == 0 
	else:
		return False

def has_three_digit_factor_tuples(number):
	i = 1000
	while i > 99:
		if divisible_by(number, i):
			other_factor = number / i
			if other_factor > 99 and other_factor < 1000:
				print i, other_factor
				return True
		i = i - 1

sixdigitnumber = 999999
count = 0
found_two_digit_factors = False
while sixdigitnumber >= 100000 and not found_two_digit_factors:
	if is_palindrome(get_digits(sixdigitnumber)):
		if has_three_digit_factor_tuples(sixdigitnumber):
			found_two_digit_factors = True
			print sixdigitnumber
	sixdigitnumber = sixdigitnumber - 1



