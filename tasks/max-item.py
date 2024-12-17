from hyperon import MeTTa

metta = MeTTa()
result = metta.run(
    """


; The following expression finds the max value from the list.
(= (find-max ()) ())
(= (find-max $list) (
    let $tail (cdr-atom $list) (if (== $tail ()) (car-atom $list) 
    (let*(
        ($head (car-atom $list))
        ($tail_new (find-max $tail))
    ) (if (< $head $tail_new) $head $tail_new))
    )
    
))
!(find-max (1 2 1 2 4 1 3))

"""
)
print(result)
