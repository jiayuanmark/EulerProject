s = set([])

for a in range(2, 101):
	for b in range(2, 101):
		s.add(str(a ** b))

print len(s)