def orth_triangle(*, hypotenuse: float = 0, catet1: float = 0, catet2: float = 0):

    if hypotenuse != 0 and catet1 != 0 and catet2 != 0:
        return None
        
    if hypotenuse == 0:
        result = round((catet1**2 + catet2**2)**0.5, 2)
        return result
            
    total = catet1 + catet2
    
    if hypotenuse > total:
        result = round((hypotenuse**2 - cathet_sum**2)**0.5, 2)
    elif hypotenuse <= total:
        result = None
    return result

# > orth_triangle(cathetus1=3, hypotenuse=5)
# 4.0
# > orth_triangle(cathetus1=8, cathetus2=15)
# 17.0
# > print(orth_triangle(cathetus2=9, hypotenuse=3))
# None
        