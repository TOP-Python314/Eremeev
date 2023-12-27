def strong_password(password: str) -> bool:
    if len(password) < 8:
        return False
    lowercase = False
    uppercase = False
    digits = 0
    special_chars = False

    for char in password:
        if char.islower():
            lowercase = True
        elif char.isupper():
            uppercase = True
        elif char.isdigit():
            digits += 1
        else:
            special_chars = True

    if lowercase and uppercase and digits >= 2 and special_chars:
        return True
    else:
        return False

# >>> strong_password('aW5;PO_24')
# True 

# >>> strong_password('password')
# False       
    
    
    