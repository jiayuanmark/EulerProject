

bound :: Integer
bound = fromIntegral . length $ takeWhile (\x -> ceiling (10 ** (1 - 1 / (fromIntegral x))) < 10) [1..]

calc :: Integer -> Integer -> Integer
calc x n = fromIntegral . length . show $ (x ^ n)

check :: Integer -> Integer -> Bool
check n x = (== n) $ calc x n

solve :: Int
solve = length $ [ x^n | x <- [1..9], n <- [1..bound], (check n x) ]

main :: IO ()
main = putStrLn $ show $ solve