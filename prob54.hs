
import Data.List.Split (splitOn)
import Data.List (intercalate, elemIndex, group, sortBy)
import Data.Maybe (fromJust)
import Control.Monad (when)

data Card = Card { getValue :: Int, getSuit :: Int }
	deriving Show

type Hand = [Card]

loadData :: FilePath -> IO ([String])
loadData fileName = do
	s <- readFile fileName
	return $ lines s


parseHand :: [String] -> Hand
parseHand str = map parseCard str
	where
		allValues = "23456789TJQKA"
		allSuits = "SHDC"
		parseValue val = fromJust $ elemIndex val allValues
		parseSuit suit = fromJust $ elemIndex suit allSuits
		parseCard [x, y] = Card (parseValue x) (parseSuit y)


solveRank :: Hand -> Int
solveRank lst
	| royal = 10
	| flush && straight = 9
	| kind 4 = 8
	| kind 3 && kind 2 = 7
	| flush = 6
	| straight = 5
	| kind 3 = 4
	| twoPair = 3
	| kind 2 = 2
	| otherwise = 1
	where
	value = map (\x -> getValue x) lst
	suit = map (\x -> getSuit x) lst
	flush = 1 == length (group suit)
	ranks = group $ sortBy (flip compare) $ value
	kind n = not $ null . filter ((n ==) . length) $ ranks
	straight = (5 == length ranks) && (4 == (maximum value - minimum value))
	royal = flush && straight && (minimum value == 8)
	twoPair = 2 == (length . filter ((2 ==) . length) $ ranks)


solveTie :: Hand -> [[Int]]
solveTie lst = map kind [4, 3, 2, 1]
	where
		value = map (\x -> getValue x) lst 
		kind n = map head $ filter ((n ==).length) $ group ranks
		ranks = sortBy (flip compare) $ value


parseGame :: [String] -> [(Hand, Hand)]
parseGame content = map (\x -> (parseHand (p1 x), parseHand (p2 x))) content
	where
		p1 = take 5 . splitOn " " 
		p2 = drop 5 . splitOn " "


processGame :: [(Hand, Hand)] -> IO ()

processGame (g:games) = do
	let (p1, p2) = g
	putStrLn $ show p1
	putStrLn $ show (solveRank p1, solveTie p1)
	putStrLn $ show p2
	putStrLn $ show (solveRank p2, solveTie p2)
	when ((solveRank p1, solveTie p1) > (solveRank p2, solveTie p2)) $ putStrLn "Player 1 win"
	processGame games

processGame [] = return ()



main :: IO ()
main = do
	input <- loadData "poker.txt"
--	processGame $ parseGame input
	putStrLn $ show $ foldr (+) 0 $ map playGame $ parseGame input
		where playGame (x, y) = if (solveRank x, solveTie x) > (solveRank y, solveTie y)
								then 1
								else 0





