

fourDigit :: [Integer] -> [Integer]
fourDigit = takeWhile (<= 9999) . dropWhile (< 1000)

triangle :: [Integer]
triangle = map round $ [ n * (n+1) / 2 | n <- [1..] ]

square :: [Integer]
square = [ n^2 | n <- [1..] ]

pentagonal :: [Integer]
pentagonal = map round $ [ n * (3*n-1) / 2 | n <- [1..] ]

hexagonal :: [Integer]
hexagonal = [ n * (2*n-1) | n <- [1..] ] 

heptagonal :: [Integer]
heptagonal = map round $ [ n * (5*n-3) / 2 | n <- [1..] ]

octagonal :: [Integer]
octagonal = [ n * (3*n-2) | n <- [1..] ]


solve = do
  