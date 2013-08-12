
def cycle_len(d):
	history = {} 
	num, cnt = 1, 0
	while True:
		digit = (num * 10) % d
		num = digit
		if history.has_key(digit):
			return cnt - history[digit]
		else:
			history[digit] = cnt
		cnt = cnt + 1


cycle = map(lambda x :cycle_len(x), range(1, 1000))
print sorted(range(1, 1000), key=lambda x:cycle[x-1], reverse=True)[0]