from string import ascii_lowercase as l

def encrypt_msg(msg, a, b):
    cipher = ""
    for char in msg:
        if char.isalpha():
            x = l.index(char.lower())
            # E(x) = (ax + b) % 26
            cipher += l[(a * x + b) % 26].upper() if char.isupper() else l[(a * x + b) % 26]
        else:
            cipher += char

    return cipher

def decrypt_msg(cipher, a, b):
    plaintext = ""
    a_inv = 0
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break

    for char in cipher:
        if char.isalpha():
            y = l.index(char.lower())
            # D(x) = (a_inv * (y - b)) % 26
            plaintext += l[(a_inv * (y - b)) % 26].upper() if char.isupper() else l[(a_inv * (y - b)) % 26]
        else:
            plaintext += char

    return plaintext

print(
"""
====================================
           Affine cipher            
====================================

Mode:

1. Encryption
2. Decryption

"""
)
mode = input("(*)> ")
a = int(input("(*)> a: "))
b = int(input("(*)> b: "))
res = ""

if int(mode) == 1 and a and b:
    msg = input("(*)> plaintext: ")
    res = encrypt_msg(msg, a, b)
elif int(mode) == 2 and a and b:
    msg = input("(*)> cipher: ")
    res = decrypt_msg(msg, a, b)

print(
f"""
    *********************************
    *             {res}               *
    *********************************
 """
)

print("                CYA <3            ")
