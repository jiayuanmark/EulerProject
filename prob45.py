N = 100000
triangle = set([ u * (u + 1) / 2 for u in range(N) ])
pentagonal = set([ u * (3*u - 1) / 2 for u in range(N) ])
hexagonal = set([ u * (2*u - 1) for u in range(N) ])

print triangle.intersection(pentagonal).intersection(hexagonal)