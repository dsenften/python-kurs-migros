#!/usr/bin/env python3

import string;

SHIFT = 3
choice = input("would you like to encode or decode? ")
word = input("Please enter text: ")
letters = string.ascii_letters + string.punctuation + string.digits

# pylint: disable=C0103
encoded = ''
if choice == "encode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) + SHIFT
            encoded = encoded + letters[x]
if choice == "decode":
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) - SHIFT
            encoded = encoded + letters[x]
print(encoded)