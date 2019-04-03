izbaci _ [] = []
izbaci 0 (x:xs) = xs
izbaci k (x:xs) = x : (izbaci (k-1) xs)


