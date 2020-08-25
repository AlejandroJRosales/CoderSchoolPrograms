text = input("Message: ")
ciphered_text = ""
for letter in text:
    ciphered_text += chr(ord(letter) + 1)
print(f"Ciphered text: {ciphered_text}")

deciphered_text = ""
for letter in ciphered_text:
    deciphered_text += chr(ord(letter) - 1)
print(f"Deciphered text: {deciphered_text}")
