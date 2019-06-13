
"""
This file is to test out some of the functions from chatbot_funct, 
the most important module of this chatbot
"""

import chatbot_funct as cf

#making sure that ending function is working
def test_end(): 
    assert cf.end_chat("Bye bye") == True
    assert cf.end_chat("quit") == True


#making sure that question judgement function is working
def test_question():
    assert cf.is_question("What are you talking about?") == True
    assert cf.is_question("How are you?") == True


#making sure that greeting judgement function is working
def test_greeting():
    assert cf.is_hi_greeting("hello!") == True
    assert cf.is_hi_greeting("hi!") == True


#making sure that the function is able to distinguish good and bad responses
def test_good_resp(): 
    assert cf.is_resp_good("not bad") == True
    assert cf.is_resp_good("pretty bad") == False
    

#making sure that the prepare_text function can translate message into machine-friendly texts
def test_prepare(): 
    assert cf.prepare_text("ALL CAPS") == "all caps"