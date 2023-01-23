# Vignere Cipher
def caesar(letter, shift):
    letter = letter.lower()
    shift %= 26
    res = ord(letter) + shift
    if res > ord('z'):
        res -= 26
    return chr(res)


def encrypt(plaintext, key):
    i = 0
    key = key.lower()
    plaintext = plaintext.lower()
    ciphertext = ''
    while i < len(plaintext):
        char = plaintext[i]
        if not char.isalpha():
            ciphertext += char
            i += 1
            continue
        shift = ord(key[i % len(key)]) - ord('a')
        ciphertext += caesar(char, shift)
        i += 1
    return ciphertext


def decrypt(ciphertext, key):
    i = 0
    plaintext = ''
    key = key.lower()
    while i < len(ciphertext):
        char = ciphertext[i]
        shift = -1 * (ord(key[i % len(key)]) - ord('a'))
        if not char.isalpha():
            plaintext += char
            i += 1
            continue
        plaintext += caesar(char, shift)
        i += 1
    return plaintext


res = encrypt("abcde", "hello")
print(f'Encrypting string abcde using key "hello" - {res}')
print(f'Decrypting {res} using key "hello" - {decrypt(res, "hello")}')

message = input('Enter message - ')
key = input('Enter key - ')
result = encrypt(message, key)
print(f'Result of encrypting {message} with key {key} is \n{result}')
plaintext = decrypt(result, key)
print(f'Result of decrypting {result} with key {key} is \n{plaintext}')
