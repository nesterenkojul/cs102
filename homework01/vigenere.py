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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    k = 0
    end = 0
    for i in range(len(plaintext)):
        if k > len(keyword) - 1:
            k = 0
        if plaintext[i].isalpha():
            index = ord(plaintext[i]) + alphabet.find(keyword[k].lower())
            if (plaintext[i].islower() and index > 122) or (plaintext[i].isupper() and index > 90):
                index -= 26
            ciphertext += chr(index)
        else:
            ciphertext += plaintext[i]
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
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    k = 0
    end = 0
    for i in range(len(ciphertext)):
        if k > len(keyword) - 1:
            k = 0        
        if ciphertext[i].isalpha():
            index = ord(ciphertext[i]) - alphabet.find(keyword[k].lower())
            if (ciphertext[i].islower() and index < 97) or (ciphertext[i].isupper() and index < 65):
                index += 26
            plaintext += chr(index)
        else:
            plaintext += ciphertext[i]
        k += 1
    return plaintext
