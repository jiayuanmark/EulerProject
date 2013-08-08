
def palindrome(num):
	s = str(num)
	left = s[0: (len(s) / 2) ]
	if len(s) % 2 == 0:
		right = s[(len(s) / 2):]
	else:
		right = s[(len(s) / 2 + 1):]
	if left == right[::-1]:
		return True
	else:
		return False


ans = 0
for i in range(999, 99, -1):
	for j in range(999, 99, -1):
		if palindrome(i*j) and i * j > ans:
			ans = i * j
print ans