

def large_num_sum(s1, s2):
	num1 = s1[::-1] if len(s1) >= len(s2) else s2[::-1]
	num2 = s2[::-1] if len(s1) >= len(s2) else s1[::-1]
	ret = ''
	carry = 0
	for idx in xrange(len(s2)):
		temp = int(num1[idx]) + int(num2[idx]) + carry
		carry = temp / 10
		ret = ret + str(temp % 10)

	for idx in xrange(len(s2), len(s1)):
		temp = int(num1[idx]) + carry
		carry = temp / 10
		ret = ret + str(temp % 10)
	
	if carry != 0:
		ret = ret + str(carry)
	return ret[::-1]

f = file('input_13', 'r')
lines = f.readlines()
print reduce(lambda x, y : large_num_sum(x, y), [ u.strip() for u in lines ])[0:10]