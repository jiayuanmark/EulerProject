

isPrime :: Integer -> Bool
isPrime num
	| num <= 1  = False
	| otherwise = all (\x -> num `mod` x /= 0) [2..round $ sqrt $ fromIntegral num]


numPrime :: Integer -> Integer
numPrime level = let
					inc = 2 * (level - 1)
					start = (inc - 1) ^ 2 + inc
				 in fromIntegral $ length $ filter isPrime $ take 4 [start, (start+inc)..]


primeRatio :: Double -> Integer
primeRatio ratio = primeRatio' 2 0
	where
		primeRatio' level count
			| r < ratio = 2 * level - 1
			| otherwise = primeRatio' (level + 1) next
			where
				primes = numPrime level
				next = count + primes
				total = 1 + 4 * (level -1)
				r = (fromIntegral next) / (fromIntegral total)

main :: IO ()
main = do
	putStrLn $ show $ primeRatio 0.10