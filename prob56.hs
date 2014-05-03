

import Data.Char (digitToInt)

digitSum :: Integer -> Integer
digitSum num = sum $ map (fromIntegral . digitToInt) $ show num


main :: IO Integer
main = return $ maximum $ map (\x -> digitSum x) [ x^y | x <- [1..99], y <- [1..99]]