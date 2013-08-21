
L = "".join([ str(u) for u in range(1, 200000) ])
idx = [1, 10, 100, 1000, 10000, 100000, 1000000 ]

print reduce(lambda x, y : x*y, map(lambda x : int(L[x-1]), idx))