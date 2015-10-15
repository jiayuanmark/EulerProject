import Data.List
import Data.Ord

rprime :: Int -> Int
rprime n = length $ filter (\x -> (== 1) $ gcd n x) [1..n]

phi :: Int -> Rational
phi = do
  d <- fromIntegral . rprime
  n <- fromIntegral
  return (n / d)

solve :: Int -> Int
solve m = fst $ maximumBy (comparing snd) $ map (\x -> (x, phi x)) [2..m]

main :: IO ()
main = putStrLn $ show $ solve 1000000