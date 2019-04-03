cifre [] = 0
cifre (x:xs) 
            | any (x == ) ['1'..'9'] = 1 + cifre xs
            | otherwise = cifre xs


mala [] = 0
mala (x:xs) 
            | any (x == ) ['a'..'z'] = 1 + mala xs
            | otherwise = mala xs


desifruj [] = []
desifruj (x:xs) = desifruj' x : desifruj xs


desifruj' (x:xs) 
            | any (x == ) ['1'..'9'] = drop (cifre (x:xs)) (x:xs)
            | any (x == ) ['a'..'z'] = drop (mala (x:xs)) xs
            | otherwise = (x:xs)