--primljeni n lst = (take n lst):[(drop n lst)]

primljeni 0 lst = [lst]
primljeni 1 (x:xs) = [x]
primljeni n (x:xs) = [x] ++ (primljeni (n-1) xs)





