# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


"Parser for kinect tools"


import random
import string
from tqdm import tqdm

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

randstring = id_generator()


found = 0;
notfound = 0

lfound = []
lnotfound = []
lnomatchatall = []
pi_init_length = 100
no_match_at_all = 0
for k in range(100000):
    for i in range(2,10000):
        ##Make longer and longer strings
        randstring = id_generator(size=i)
        ##Convert to ASCII
        #ascii = [ord(c) for c in randstring]
        ascii = ''.join(str(ord(c)) for c in randstring)
        currentnotfound = 0 
        for j in range(1,pi_init_length):
            try:
                # import version included with old SymPy
                from sympy.mpmath import mp
            except ImportError:
                # import newer version
                from mpmath import mp
            mp.dps = j*10  # set number of digits
            stt = mp.pi
            if ascii in str(stt):
                found = found +1;
                lfound.append([i,j])     
                print("match with string length " + str(i)+ " and pi length: " +str(j*10)+ " with string " + randstring)
                break;
            else:
                notfound = notfound + 1;
		currentnotfound = currentnotfound +1;
                lnotfound.append([i,j*10])
        if currentnotfound == 99:
            print("NO MATCH for string: " + str(randstring))
            pi_init_length = pi_init_length*2
            no_match_at_all = no_match_at_all +1;
            lnomatchatall.append([i,j*10])
    #print(mp.pi)   # print pi to a thousand places
    
    
