

isPrime :: Integer -> Bool
isPrime num
	| num <= 1  = False
	| otherwise = all (\x -> num `mod` x /= 0) [2..round $ sqrt $ fromIntegral num]


isPrimeSet :: [Integer] -> Bool
isPrimeSet lst = all isPrime combination
	where combination = [ read $ shows x $show y) | x <- lst, y <- lst, x /= y ]


searchPrime :: Integer -> Integer
searchPrime n = minimum $ map sum $ filter isPrimeSet candidate
	where
		primes = filter isPrime [2..n]
		candidate = [[x, y, z, u, v] | x <- primes, y <- primes, z <- primes, u <- primes, v <- primes, x < y, y < z, z < u, u < v ]