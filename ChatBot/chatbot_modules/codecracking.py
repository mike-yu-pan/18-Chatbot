
"""
This module allows our chatbot to decipher an encoded message even if nobody knows the key
"""

def attempt(msg, key = 0):
    """takes in an string and a key(default as 0), translate the string according to the key's value"""

    decode = ""

    for char in msg:
        new_char = chr(ord(char) - key)
        decode += new_char
    return decode


def crack(code):
    """takes in an string, repeatedly using attempt() while increasing the value of the key after each attempt until the string contains all of the following element: " ", "a" or "A", "e" or "E", or until the key's value exceed 50000"""

    trying = True
    key = 0

    while trying == True:

        decode = attempt(code, key)
        key += 1
        print(decode)

        if " " in decode:
            if "a" or "A" in decode:
                if "e" or "E" in decode:
                    print("-We've cracked it, boss, the key is " + str(key - 1) + " and your silly lil secret message is:\n \"" + decode + "\"")
                    trying = False
                    break

        if key >= 50000:
            trying = False
            print("-sorry boss can\'t crack the code")


def exe(): 
    """executes the codecracking function"""

    to_crack = input("-enter your encrypted message here: ")
    if to_crack == "quit":
        print("-if you say so, boss")
    else:
        crack(to_crack)
