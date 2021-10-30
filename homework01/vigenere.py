def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    k = 0
    for i, letter in enumerate(plaintext):
        k = 0 if k > len(keyword) - 1 else k
        if letter.isalpha():
            index = ord(letter) + ord(keyword[k].lower()) - ord("a")
            if (letter.islower() and index > ord("z")) or (letter.isupper() and index > ord("Z")):
                index -= 26
            ciphertext += chr(index)
        else:
            ciphertext += letter
        k += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    k = 0
    for i, letter in enumerate(ciphertext):
        k = 0 if k > len(keyword) - 1 else k
        if letter.isalpha():
            index = ord(letter) - ord(keyword[k].lower()) + ord("a")
            if (letter.islower() and index < ord("a")) or (letter.isupper() and index < ord("A")):
                index += 26
            plaintext += chr(index)
        else:
            plaintext += letter
        k += 1
    return plaintext
