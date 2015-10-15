import Data.Array (accumArray, (!))

minus :: (Ord a) => [a] -> [a] -> [a]
minus (x:xs) (y:ys) = case (compare x y) of 
  LT -> x : minus xs (y:ys)
  EQ -> minus xs     ys
  GT -> minus (x:xs) ys
minus xs _     = xs

sieve :: Int -> [Int]
sieve m = eratos [2..m]
  where
    eratos []     = []
    eratos (p:xs) = p : eratos (xs `minus` [p*p, p*p+p..m])

searchPrime :: Int -> [[Int]]
searchPrime n = do
  a <- cand
  let u = f a $ dropWhile (<= a) cand
  b <- u
  let v = f b $ dropWhile (<= b) u
  c <- v
  let w = f c $ dropWhile (<= c) v
  d <- w
  let x = f d $ dropWhile (<= d) w
  e <- x
  return [a, b, c, d, e]
  where
    primes  = sieve (n * n)
    cand    = takeWhile (<= n) primes
    arr     = accumArray (||) False (1, n * n) [ (i, True) | i <- primes ]
    f x     = filter (\y -> and [ arr ! (read $ shows x $show y),
                                  arr ! (read $ shows y $show x) ])

main :: IO ()
main = do
  let sol = sum $ head $ searchPrime 10000
  putStrLn $ show sol
