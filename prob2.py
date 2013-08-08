
lst = [1, 2]
while True:
	num = lst[-1] + lst[-2]
	if num > 4000000:
		break
	lst.append(num)

print sum(filter(lambda x : x % 2 == 0, lst))