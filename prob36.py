
def palindrome(s):
	left = s[0: (len(s) / 2) ]
	if len(s) % 2 == 0:
		right = s[(len(s) / 2):]
	else:
		right = s[(len(s) / 2 + 1):]
	if left == right[::-1]:
		return True
	else:
		return False

def binom_palin(num):
	return palindrome(str(num)) and palindrome(bin(num)[2:])

print sum(filter(lambda x : binom_palin(x), range(1000000)))