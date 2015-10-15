import Control.Monad
import qualified Data.List as L
import qualified Data.Set as S

fourDigit :: [Int] -> [Int]
fourDigit = takeWhile (<= 9999) . dropWhile (< 1000)

triangle :: [Int]
triangle = [ n * (n+1) `div` 2 | n <- [1..] ]

square :: [Int]
square = [ n^2 | n <- [1..] ]

pentagonal :: [Int]
pentagonal = [ n * (3*n-1) `div` 2 | n <- [1..] ]

hexagonal :: [Int]
hexagonal = [ n * (2*n-1) | n <- [1..] ] 

heptagonal :: [Int]
heptagonal = [ n * (5*n-3) `div` 2 | n <- [1..] ]

octagonal :: [Int]
octagonal = [ n * (3*n-2) | n <- [1..] ]

check :: [Int] -> Bool
check lst = (length edgelst == 6) && (s1 == s2)
  where
    src     = zip (map (`div` 100) lst) [1,2..]
    dst     = zip (map (`mod` 100) lst) [1,2..]
    edgelst = L.nub $ [ (min i j, max i j) | (u, i) <- src, (v, j) <- dst, u == v, i /= j ]
    s1      = S.fromList $ map fst edgelst
    s2      = S.fromList $ map snd edgelst

solve :: [[Int]]
solve = filter check ls
  where ls = [ [a, b, c, d, e, f] | a <- fourDigit triangle,
                                    b <- fourDigit square,
                                    c <- fourDigit pentagonal,
                                    d <- fourDigit hexagonal,
                                    e <- fourDigit heptagonal,
                                    f <- fourDigit octagonal ]
main :: IO ()
main = do
  putStrLn $ show $ head $ solve
