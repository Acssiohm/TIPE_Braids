# Braids Homotopy 

## Create a Braid
Each generator of the Braids group is associated with its number ( strictly positive ), its inverse is associated with the oppsit of the number, and 0 represents the neutral element :
- sigma_k -> k
- sigma_k^-1 -> -k
- epsilon -> 0
Then a braid is a word on those elements, that we represent with a list :
sigma_i.sigma_j.sigma_k^-1  -->  `[i, j, -k]`
Thus to create a braid, with l its associated list you can do :
`b = Braid(l)`

## Operations on braids 
`b1 = Braid(l1)
b2 = Braid(l2)`
- Concatenation / product : `b_product = b1*b2`
- Power : `b_power_k = b**k`
    Note that the power can be negative or zero ( but must be an integer )
- Divison : `b_fraction = b1/b2`
- Comparison/Test equivalence : `is_equivalent = (b1 == b2)`
- Methods of testing homotopy :
    - "Retournement de sous-mots" : `b.retournement_sous_mots()`
    - "Réduction de poignées"(default) : `b.reduction_poignees()`
- Print :
    Example : `b = Braid([1, 2, 0, -2])`
    - Replacing with letters (default) : 
         `print(b)` or `print(b.to_letters())` prints `ab.B`
    - With numbers :
        `print(b.to_string())` prints `(1)(2)(0)(-2)`
 
