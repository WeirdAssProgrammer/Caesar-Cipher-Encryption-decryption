# Caesar cipher implemntation

print(
"""
====================================
			Caesar cipher			
====================================

Mode:

1. Encryption
2. Decryption

"""
)
mode = input("(*)> ")
key = input("(*)> Key: ")
if int(mode) == 1 and key:
	msg = input("(*)> plaintext: ")
	print(encryption(msg, key))
elif int(mode) == 2 and key:
	msg = input("(*)> cipher: ")
	print(decryption(msg, key))
from string import ascii_letters as l
def encryption(msg, key):
	cipher = ""
	for char in msg:
		x = list(l).index(char)
		#ek(x) = x + k % 26
		cipher += l[(x + key) % 26]

	return cipher
def decryption(cipher, key):
	plaintext = ""
	for char in cipher:
		y = list(l).index(char)
		#dk(x) = y - k % 26
		plaintext += l[(y - key)%26]
	return plaintext

