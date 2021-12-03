def is_real(n: str) -> bool:
    """
    Tests to see if a string is real number.
    >>> is_real("0.000")
    False
    >>> is_real("0.001")
    True
    >>> is_real("3.000")
    False
    >>> is_real("2.001")
    True
    >>> is_real("0.w3333")
    False
    >>> is_real("0")
    True
    >>> is_real("0.000.")
    False
    >>> is_real(".32")
    False
    >>> is_real("1.2.3.re")
    False
    """
    if n.isdigit() and (n[0] != '0' or n == '0'):
            return True
    if n.count('.') == 1:
        if n.find('.') != 0 and n.find('.') != len(n) - 1:
            if n.replace('.', '').isdigit() and n[-1] != '0':
                return True
    return False
    

def check_password(password: str) -> bool:
    """
    Tests to see if a password is valid.
    >>> check_password("h^*&ITY8")
    False
    >>> check_password("568ftygvh^*&ITYGHrdtu43f")
    True
    >>> check_password("5817278219213901421")
    False
    >>> check_password("frewrg3451gerw354???")
    False
    >>> check_password("SYEHDF568FGHmhvnb78")
    False
    """
    if len(password) < 16:
        return False
        
    if password.isalnum():
        return False
        
    alphas = any(filter(str.isalpha, list(password)))    
    if not alphas or password.islower() or password.isupper():
        return False
 
    digits = any(filter(str.isdigit, list(password)))    
    if not digits:
        return False
    return True
        