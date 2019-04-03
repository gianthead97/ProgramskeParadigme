import Debug.Trace

broj [] = True 
            
broj (x:xs) 
            |  any (x ==) ['1'..'9'] = broj xs 
            |  otherwise = False 
            

mala [] = True

mala (x:xs) 
            | any (x == ) ['a'..'z'] = mala xs
            | otherwise = False



sifruj [] = []            
sifruj (x:xs) 
            | broj x = (['C'] ++ x ++ ['C']) : sifruj xs
            | mala x = (['M'] ++ x ++ ['M']) : sifruj xs
            | otherwise = x : sifruj xs
