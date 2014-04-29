

isPrime :: Integer -> Bool
isPrime x 
	| x <= 1 	= False
	| otherwise = isPrime' x 2
	where isPrime' num div = if div * div > num
							 then True
							 else (num `mod` div /= 0) && isPrime' num (div+1)


replaceDigit :: String -> Char -> Char -> String
replaceDigit [] _ _ = error "empty number"
replaceDigit all@(x:xs) old new 
	| x == old && new == '0' = "0"
	| otherwise = map (\dig -> if dig == old then new else dig) all


genSequence :: String -> Char -> [Integer]
genSequence num old
	| old `elem` num = filter (\x -> isPrime x) (map (\x -> read x) replaced)
	| otherwise = []
	where replaced = map (\x -> replaceDigit num old x) ['0'..'9']


testPrimeFam :: Integer -> Int -> Bool
testPrimeFam x len 
	| length cand < len = False
	| otherwise = any (\lst -> (length lst) >= len) (map (\old -> genSequence num old) cand)
	where
		num = show x
		cand = [minimum num..'9']


searchFam :: Int -> Integer
searchFam len = searchFam' l len
				where l = [y | y <- [2..], isPrime y]


searchFam' :: [Integer] -> Int -> Integer
searchFam' (x:xs) len = if testPrimeFam x len
						then x
						else searchFam' xs len