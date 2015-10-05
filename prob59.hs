import Data.List.Split (splitOn)
import Data.Bits (xor)
import Data.Char (ord, chr, isPrint)
import System.IO
import Data.List (intercalate)
import Data.Maybe

loadData :: FilePath -> IO String
loadData filename = do
	content <- readFile filename
	return $ content


tokenize :: String -> [Int]
tokenize ln = map read $ splitOn "," ln


profile :: String -> Bool
profile content = any (\x -> x `elem` words) tokens
	where
		tokens = splitOn " " content
		words = [ "is", "the", "are" ]


decrypt :: [Int] -> [Int] -> Maybe String
decrypt text key =
	if (all isPrint dtext) && (profile dtext)
	then Just dtext
	else Nothing
	where dtext = map chr $ zipWith xor text $ cycle key


crack :: [Int] -> [String]
crack text = map fromJust $ filter (\x -> x /= Nothing) candidate
	where
		set = map ord ['a'..'z']
		keyset = [ [x,y,z] | x <- set, y <- set, z <- set ]
		candidate = map (decrypt text) keyset


main :: IO ()
main = do
	content <- loadData "cipher1.txt"
	let trial = tokenize content
	let text = head $ crack trial
	putStrLn $ text
	putStrLn $ show $ sum $ map ord text
	
		



