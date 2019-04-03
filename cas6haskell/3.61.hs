pozicije _ [] = []
pozicije x lst = [i | (y, i) <- zip lst [0..], y == x]