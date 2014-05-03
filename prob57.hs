
import Data.Ratio

transform :: Rational -> Rational
transform r = 1 / (r + 2) 

genSeq :: Int -> [Rational]
genSeq n = map (1 +) $ take n $ iterate transform (1 % 2)

main :: IO Int
main = return $ length $ filter compareDigits $ genSeq 1000
			where compareDigits r = (length . show $ numerator r) > (length . show $ denominator r)


