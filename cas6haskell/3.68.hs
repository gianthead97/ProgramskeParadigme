ucesljaj l [] = l
ucesljaj [] l = l
ucesljaj (x:xs) (y:ys) = [x] ++ [y] ++ (ucesljaj xs ys)