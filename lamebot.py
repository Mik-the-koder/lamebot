""" This is a work in progress, also my first GitHub release !

    to get cleverbot API on your computer `pip install cleverbot` 
    to get espeak on your computer use your package manager of choise

    made by Mik-the-Koder
"""

import os
from cleverbot import Cleverbot

try:

# variables and stuff

    Jack = Cleverbot ()
    Jill = Cleverbot ()
    JackQ = raw_input ('Enter start text: ')
# LoopVar = to control loop
    LoopVar = True
    Speech2Txt = "kek"

# main loop stuff
# JackQ = the question Jack is going to ask Jill
# JillQ = the question Jill is going to ask Jack

    while LoopVar:
        try:
            JillQ = Jack.ask (JackQ)
            Speech2Txt = 'echo "' + JackQ + '" | espeak -v +m1 '
            print 'Jack: ' + JackQ
            os.system (Speech2Txt)
    
            JackQ = Jill.ask (JillQ)
            Speech2Txt = 'echo "' + JillQ + '" | espeak -v +f1'
            print 'Jill: ' + JillQ
            os.system (Speech2Txt)
        except KeyboardInterrupt:
            LoopVar = False        

except KeyboardInterrupt:
    print 'BYE!'

