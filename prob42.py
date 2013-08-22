from math import sqrt

def IsTriangle(word):
	val = sum([ ord(u) - ord('A') + 1 for u in word ])
	num = int(sqrt(2 * val))
	return num * (num + 1) == 2 * val


if __name__ == "__main__":
	f = file("words.txt", "r")
	content = f.readline()
	words = [ u[1:-1] for u in content.split(",") ]
	print len(filter(lambda x : IsTriangle(x), words))