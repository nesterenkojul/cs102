import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            index = ord(plaintext[i]) + shift
            if (plaintext[i].islower() and index > 122) or (
                plaintext[i].isupper() and index > 90
            ):
                index -= 26
            ciphertext += chr(index)
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            index = ord(ciphertext[i]) - shift
            if (ciphertext[i].islower() and index < 97) or (
                ciphertext[i].isupper() and index < 65
            ):
                index += 26
            plaintext += chr(index)
        else:
            plaintext += ciphertext[i]
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    shift = 0
    while True:
        plaintext = ""
        for i in range(len(ciphertext)):
            if ciphertext[i].isalpha():
                index = ord(ciphertext[i]) - shift
                if (ciphertext[i].islower() and index < 97) or (
                    ciphertext[i].isupper() and index < 65
                ):
                    index += 26
                plaintext += chr(index)
            else:
                plaintext += ciphertext[i]
        if plaintext in dictionary:
            break
        shift += 1
    best_shift = shift
    return best_shift
