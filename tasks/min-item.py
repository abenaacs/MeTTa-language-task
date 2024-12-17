from hyperon import MeTTa

metta = MeTTa()
result = metta.run(
    """


; The following expression finds the min value from the list.
(= (find-min ()) ())
(= (find-min $list) (
    let $tail (cdr-atom $list) (if (== $tail ()) (car-atom $list) 
    (let*(
        ($head (car-atom $list))
        ($tail_new (find-min $tail))
    ) (if (< $head $tail_new) $head $tail_new))
    )
    
))
!(find-min (1 2 0 2 4 1 3))

"""
)
print(result)
