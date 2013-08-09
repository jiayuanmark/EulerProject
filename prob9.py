import sys

for a in xrange(500):
	for b in xrange(a+1, 500):
		c = 1000 - a - b
		if a * a + b * b == c * c:
			print a * b * c
			sys.exit(1)
