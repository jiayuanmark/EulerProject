from math import sqrt


def is_prime(num):
	for i in range(2, int(sqrt(num))+1):
		if num % i == 0:
			return False
	return True

def prime_len(a, b):
	n = 2
	while True:
		if n * n + a * n + b <= 0:
			return n-1  
		if is_prime(n * n + a * n + b):
			n = n + 1
		else:
			return n-1


table = [ True ] * 3000
table[0] = table[1] = False

for i in range(2, int(sqrt(3000)) + 1):
	if not table[i]:
		continue
	for j in range(2, 3000 / i):
		table[i * j] = False

b_candidate = filter(lambda x: table[x] == True, range(2, 1000))


max_len, ans = 1, -1
for b in b_candidate:
	for a in range(-1000, 1000):
		if table[a + b + 1] == True and prime_len(a, b) > max_len:
			max_len = prime_len(a, b)
			ans = a * b

print ans, max_len

