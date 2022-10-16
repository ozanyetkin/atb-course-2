# Sifreli mesajda her sayi bir harfe denk geliyor, mesajda ne yazdigini bulacagiz
import string

encoded_str = "6 14 14 3,9 14 1,8 13,3 4 2 17 24 15 19 8 13 6,19 7 8 18"
alphabet = string.ascii_uppercase

"""
i = 1
for letter in alphabet:
    print(i, letter)
    i += 1
"""

"""
alphabet_decoder = {}
for i, letter in enumerate(alphabet):
    alphabet_decoder[letter] = i + 1
"""
def caesar_decoder(encoded_str, shift=5):
    alphabet_decoder = {}
    for i, letter in enumerate(alphabet):
        alphabet_decoder[i + shift] = letter

    decoded_str = ""
    for word in encoded_str.split(","):
        for letter in word.split(" "):
            decoded_str += alphabet_decoder[int(letter)]
        decoded_str += " "
    return decoded_str
# print(decoded_str)

alphabet_encoder = {}
for i, letter in enumerate(alphabet):
    alphabet_encoder[letter] = i + 5

"""
encoded_str = ""
for letter in decoded_str:
    if letter == " ":
        encoded_str += ","
    else:
        encoded_str += str(alphabet_encoder[letter]) + " "
"""
decoded_str = "AFERIN SIFREYI COZDUN"

decoded_words = decoded_str.split(" ")
print(decoded_words)
encoded_str = ""
for word in decoded_words:
    encoded_word = ""
    if len(word) > 0:
        for letter in word:
            encoded_word += str(alphabet_encoder[letter]) + " "
        encoded_str += encoded_word.strip()
        encoded_str += ","

encoded_str = encoded_str[:len(encoded_str) - 1]
print(encoded_str)

print(caesar_decoder(encoded_str))
