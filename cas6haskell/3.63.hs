brisiPonavljanja [x] = [x]
brisiPonavljanja (x:xs) = let bez_duplikata = brisiPonavljanja xs in
                            if (any (x == ) bez_duplikata)
                                then bez_duplikata
                                else x : bez_duplikata