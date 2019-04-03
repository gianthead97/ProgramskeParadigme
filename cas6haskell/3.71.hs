magicniParovi lst = zip lst (map calculate lst)

calculate x = product (brojUListu x)

brojUListu 0 = []
brojUListu  x = (brojUListu (x `div` 10)) ++ [x `mod` 10]