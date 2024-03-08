import random
import string

chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()

random.shuffle(key)


# print(chars)
# print(key)

plain_text = input("Enter a message: ")
cipher_text= ""

for letter in plain_text:
    index=chars.index(letter)
    cipher_text += key[index]



print(f"Original Message : {plain_text}")
print(f"Encrption Message : {cipher_text}")


cipher_text= input("Enter a cipher_text: ")
plain_text = ""

for letter in cipher_text:
    index=key.index(letter)
    plain_text += chars[index]



print(f"Original Message : {cipher_text}")
print(f"Decrption Message : {plain_text}")
