import Data.List


prosekOdlicni lst = realToFrac (sum (filtrirajOdlicne lst)) / (realToFrac (length (filtrirajOdlicne lst)))

filtrirajOdlicne lst = filter (>4.5) (map prosek lst)

prosek lst =  realToFrac (sum lst) /  realToFrac (length lst)