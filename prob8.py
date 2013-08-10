

with file('input_8', 'r') as f:
	s = ''.join([ u.strip() for u in f.readlines() ])
	s = s.strip()

print len(s)

ans = 0
for item in xrange(4, len(s)):
	num = reduce(lambda x, y : x * y, [ int(s[x]) for x in range(item-4, item+1) ])
	if num > ans:
		ans = num
print ans