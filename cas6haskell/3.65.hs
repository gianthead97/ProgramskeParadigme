broj [] = 0
broj (x:xs) = x * 10^(length xs) + broj xs


obrnutiBroj lst = broj (reverse lst)
