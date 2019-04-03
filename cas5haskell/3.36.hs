ubaci 0 n lista = n:lista
ubaci k n [] = [n]
ubaci k n (x:xs) = x:(ubaci k (n-1) xs)