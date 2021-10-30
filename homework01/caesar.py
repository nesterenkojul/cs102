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
    for i, letter in enumerate(plaintext):
        if letter.isalpha():
            index = ord(letter) + shift
            if (letter.islower() and index > ord("z")) or (letter.isupper() and index > ord("Z")):
                index -= 26
            ciphertext += chr(index)
        else:
            ciphertext += letter
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
    for i, letter in enumerate(ciphertext):
        if letter.isalpha():
            index = ord(letter) - shift
            if (ciphertext[i].islower() and index < ord("a")) or (
                ciphertext[i].isupper() and index < ord("A")
            ):
                index += 26
            plaintext += chr(index)
        else:
            plaintext += letter
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    shift = 0
    while True:
        plaintext = ""
        for i, letter in enumerate(ciphertext):
            if letter.isalpha():
                index = ord(letter) - shift
                if (ciphertext[i].islower() and index < ord("a")) or (
                    ciphertext[i].isupper() and index < ord("A")
                ):
                    index += 26
                plaintext += chr(index)
            else:
                plaintext += letter
        if plaintext in dictionary:
            break
        shift += 1
    return shift
