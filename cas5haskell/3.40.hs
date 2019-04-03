import Debug.Trace


--usteda :: (Float a, Integral a) => [a] -> a

usteda [] = 0
usteda (x:xs) | (&&) (x - ((floor x)::Float) == 0)  ( round x `mod` 25 == 0) = ((round x `div` 2) + usteda xs)
              | otherwise = (x + usteda xs)
