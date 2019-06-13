
"""
This module allows the chatbot to roll a dice
"""

import random

def roll(size):
    """takes in an integer, randomly returns a number in the range of 1 to that integer(inclusive)"""
    
    size = range(1, size + 1)
    result = random.choice(size)
    print(result)


def type_error():
    """randomly returns a phrase from the dictionary retrn_lst"""

    retrn_lst = ["-Haha, good one, please try again", "LOL, seriously though", "Please try again"]
    return random.choice(retrn_lst)


def exe(): 
    """execute the dice function"""

    running = True

    while running:
        in1 = input("-Enter how many sides do you want the dice to have(don\'t even think about a decimal number): ")
        if in1 == "quit":
            running = False
            roll_again = False

        while running:
            
            if "." in in1:
                print("-How about you find me a dice with " + in1 + " sides?")

            try:
                size = int(in1)
                roll(size)
                roll_again = True
                break

            except:
                print(type_error())
                roll_again = False
                break

        while roll_again:
            in2 = input("-Wanna roll this dice again?(Y/N): ")
            if in2 == "N" or in2 == "n":
                roll_again = False
            elif in2 == "Y" or in2 == "y" or in2 == "":
                roll(size)
            elif in2 == "quit":
                roll_again = False
                running = False
            else:
                print(type_error())
