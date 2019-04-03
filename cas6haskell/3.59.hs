varijacije xs 0 = [[]]

varijacije xs k = let ys = varijacije xs (k-1) 
                    in concat (map (\ x ->  map (x:)  ys) xs)