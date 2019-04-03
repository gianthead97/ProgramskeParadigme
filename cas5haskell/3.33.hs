spoji lst_of_lst | length lst_of_lst == 1 = head lst_of_lst
                | otherwise = (head lst_of_lst) ++ spoji (tail lst_of_lst)
                




