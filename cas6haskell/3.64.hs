podlistePonavljanja [] = []

podlistePonavljanja (x:xs) = (takeWhile (x==) xs ++ [x]) : podlistePonavljanja (dropWhile (x==) xs)  