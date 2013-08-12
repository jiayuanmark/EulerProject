
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

F = {}
F[1] = '1'
F[2] = '1'
cnt = 3
while True:
	num = large_num_sum(F[cnt-1], F[cnt-2])
	if len(num) >= 1000:
		print cnt
		break
	F[cnt] = num
	cnt = cnt + 1 