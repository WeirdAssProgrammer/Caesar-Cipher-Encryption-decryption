# Caesar cipher implemntation
from string import ascii_letters as l
def encrypt_msg(msg, key):
	cipher = ""
	for char in msg:
		x = list(l).index(char)
		#ek(x) = x + k % 26
		cipher += l[(x + key) % 26]

	return cipher
def decrypt_msg(cipher, key):
	plaintext = ""
	for char in cipher:
		y = list(l).index(char)
		#dk(x) = y - k % 26
		plaintext += l[(y - key)%26]
	return plaintext
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
key = int(input("(*)> Key: "))
res = ""
if int(mode) == 1 and key:
	msg = input("(*)> plaintext: ")
	res = encrypt_msg(msg, key)
if int(mode) == 2 and key:
	msg = input("(*)> cipher: ")
	res = decrypt_msg(msg, key)

print(
f"""
	*********************************
	*		   {res}		*
	*********************************
 """
)

print("				CYA <3			")
