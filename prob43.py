from itertools import permutations

def IsValid(S):
	if int(S[1:4]) % 2 != 0:
		return False
	elif int(S[2:5]) % 3 != 0:
		return False
	elif int(S[3:6]) % 5 != 0:
		return False
	elif int(S[4:7]) % 7 != 0:
		return False
	elif int(S[5:8]) % 11 != 0:
		return False
	elif int(S[6:9]) % 13 != 0:
		return False
	elif int(S[7:10]) % 17 != 0:
		return False
	else:
		return True


if __name__ == "__main__":
	L = "0123456789"

	print sum(map(lambda x : int(x), filter(lambda x : IsValid(x), map(lambda x : "".join(x), permutations(L, 10)))))