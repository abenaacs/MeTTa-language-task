from hyperon import MeTTa

metta = MeTTa()
result = metta.run(
    """


; The following expression appends an item
  (= (front-append $list $x)
    (cons-atom $x $list)
)
!(front-append 7 (1 2 1 2 4 1 3))

"""
)
print(result)
