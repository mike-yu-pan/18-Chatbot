
"""
This module is required maily for the user responsive judgements. 
It enables the chatbot to judge: 
-if the user response is a question, greeting, or both
-if the user wishes the chatbot to perform a task
-if the user types in nonesense
......
"""

import string
import random
import phrase_list as pl

def remove_punct(text): 
    out_string = ""
    
    for char in text: 
        if char not in string.punctuation: 
            out_string += char
    return out_string


def is_hi_greeting(text): 
    out = False
    for ele in pl.hi_greeting: 
        if ele in text: 
            out = True
    return out


def is_ques_greeting(text): 
    out = False
    for ele in pl.ques_greeting: 
        if ele in text: 
            out = True
    return out


def is_question(text): 
    out = False
    if "?" in text: 
        out = True
    elif is_ques_greeting: 
        out = True
    else: 
        out = False
    return out


def prepare_text(text): 
    out_string = ""
    remove_punct(text)

    for char in text: 
        out_string += char.lower()
    return out_string


def end_chat(text): 
    out = False
    for ele in pl.end_cmm: 
        if ele in text: 
            out = True

    for ele in pl.nothing_lst: 
        if ele == text: 
            out = True
    
    return out


def is_encode(text): 
    for ele in pl.encode_lst:
        if ele in text: 
            return True


def is_decoding(text): 
    for ele in pl.decode_lst: 
        if ele in text: 
            return True


def is_codecracking(text): 
    for ele in pl.code_crack: 
        if ele in text: 
            return True

        
def is_dice(text): 
    for ele in pl.dice_lst: 
        if ele in text: 
            return True


def what_else(): 
    print("-What else can I do for you?(decipher, encipher, or throw a dice)")


def is_greeting(text): 
    out = False
    all_greeting = pl.hi_greeting + pl.ques_greeting
    for ele in all_greeting: 
        if ele in text: 
            out = True
    return out


def is_tasking(text): 
    out = False
    all_task = pl.encode_lst + pl.code_crack + pl.decode_lst + pl.dice_lst
    for ele in all_task: 
        if ele in text: 
            out = True
    return out


def is_resp_good(text): 
    all_resp = pl.bad_greet_resp + pl.good_greet_resp
    for ele in all_resp: 
        if "not" in text: 
            if ele in text: 
                if ele in pl.bad_greet_resp: 
                    return True
                elif ele in pl.good_greet_resp: 
                    return False
                else: 
                    break
        else: 
            if ele in text: 
                if ele in pl.bad_greet_resp: 
                    return False
                elif ele in pl.good_greet_resp: 
                    return True


def conscious_ques(text): 
    for ele in pl.conscious: 
        if ele in text: 
            return True


def not_understand(text): 
    if not is_question(text): 
        if not is_greeting(text): 
            if not is_tasking(text): 
                return True