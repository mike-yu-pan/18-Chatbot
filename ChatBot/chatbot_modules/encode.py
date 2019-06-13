
"""
This module allows the chatbot to perform the most basic enciphering and deciphering
"""

import random

random_key = random.choice(range(0, 10000))

def encode(msg, key = 0):
    """takes in a string and an integer, encode the message according to the key"""
    
    encoded = ""

    for ind in msg:
        val = int(key) + ord(ind)
        encoded += chr(val)

    print(encoded)


def decode(encoded, key = 0): 
    """takes in a string and an integer, translate the encoded message according to the kwy"""

    decoded = ""

    for char in encoded: 
        val = ord(char) - int(key)
        decoded += chr(val)

    print(decoded)


def exe(): 
    """executes the encoding function"""

    msg = input("-Please enter your message here: ")
    print("(-Don't be hesitant to choose random key! I can recover your message with my codecracking ability!\nAs long as it's not a relatively short phrase)")
    key = input("-Please enter your key(an integer) here or enter \"random\" for a random key: ")
    print("-Your ciphered message is: ")

    if "random" in key:
        encode(msg, random_key)
    else:
        encode(msg, key)

def exe_decode(): 
    """executes the decoding function"""

    code = input("-Please enter your ciphered message: ")
    key = input("-Please enter your key: ")
    print("-Your message is: ")
    decode(code, key)