

import System.IO

isPalindrome :: Integer -> Bool
isPalindrome num = (show num) == reverse (show num)

rev :: Integer -> Integer
rev = read . reverse . show

isLychrel :: Integer -> Bool
isLychrel num = isLychrel' 0 num
  where isLychrel' i num
    | i > 50 = True
    | isPalindrome next = False
    | otherwise = isLychrel' (i+1) next
    where next = num + rev num

main :: IO ()
main = do
  putStrLn $ show $ length $ filter isLychrel [1..10000]