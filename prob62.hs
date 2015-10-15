import Data.List
import Data.Maybe (fromJust)

solve :: Int
solve = fromJust $ elemIndex (head (head solns)) perms
  where
    cubes  = map (^ 3) [0..10000]
    perms  = map (sort . show) cubes
    solns  = filter ((== 5) . length) . group $ sort perms

main :: IO ()
main = do
  putStrLn $ show $ (^3) solve