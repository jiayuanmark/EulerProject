

def score(name):
	return sum(map(lambda x: ord(x) - ord('A') + 1, name))

f = file('input_22', 'r')
lines = "".join(f.readlines())
names = sorted([ u[1:-1] for u in lines.split(',') ])
lst = zip(names, range(1, len(names)+1))

print sum(map(lambda x: x[1] * score(x[0]), lst))


