par n = (n-1, n+1)

postojiPar [] n = False
postojiPar lst n | (head lst) == (par n) = True
                 | otherwise = postojiPar (tail lst) n