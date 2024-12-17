from hyperon import MeTTa

metta = MeTTa()
result = metta.run(
    """


; The following expression removes an item from any postion 
  (= (concat $x $list)
   (cons-atom $x $list)
)
(= (remove () $x) ())
(= (remove $list $x)
( let*(
    ($head (car-atom $list))
    ($tail (cdr-atom $list))
    ($neat (if (== $head $x) (remove $tail $x) (concat $head (remove $tail $x))) )
) $neat )
)
!(remove (1 2 1 2 4 1 3) 1)




"""
)
print(result)
