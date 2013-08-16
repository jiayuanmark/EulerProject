import sys

def check(numer, denom):
	if numer % 10 == 0 and denom % 10 == 0:
		return False
	s1, s2 = str(numer), str(denom)
	val = float(numer) / float(denom)
	if s1[1] == s2[1] and s2[0] != '0' and float(s1[0]) / float(s2[0]) == val:
		return True
	elif s1[0] == s2[0] and s2[1] != '0' and float(s1[1]) / float(s2[1]) == val:
		return True
	elif s1[0] == s2[1] and s2[0] != '0' and float(s1[1]) / float(s2[0]) == val:
		return True
	elif s1[1] == s2[0] and s2[1] != '0' and float(s1[0]) / float(s2[1]) == val:
		return True
	return False

def euclid(a, b):
	if b == 0:
		return a
	return euclid(b, a % b);

ans = []
for numerator in range(10, 100):
	for denominator in range(numerator+1, 100):
		if check(numerator, denominator):
			ans.append((numerator, denominator))
			if len(ans) == 4:
				num = reduce(lambda x, y: x*y, [ u[0] for u in ans ])
				dnm = reduce(lambda x, y: x*y, [ u[1] for u in ans ])
				print dnm, num, dnm / euclid(dnm, num)
				sys.exit(0)

