compress = map kompresuj 
kompresuj vrsta  =  let broj_nula = length $ filter (0 ==) vrsta;
						broj_jedinica = length $ filter (1 ==) vrsta;
						indeksirano =  zip vrsta [0..]
					in  if broj_nula >  broj_jedinica 
						then (1, snd $ unzip $ filter (\x -> 1 ==  fst x) indeksirano)
						else (0, snd $ unzip $ filter (\x -> 0 ==  fst x) indeksirano)




decompress lst n = map (\x -> dekompresuj x n) lst
dekompresuj vrsta n = let broj = if (fst vrsta) ==  1 then 0 else 1;
					   indeksi = snd vrsta
					in map (\x -> if (elem (snd x) indeksi) then (fst vrsta) else broj) $ zip (replicate n broj)  [0..]
