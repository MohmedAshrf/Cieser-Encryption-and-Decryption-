#!/usr/bin/env python
# coding: utf-8

# # Cieser algorithm
# ## Encryption

# In[3]:


import string
import sys
def n_alpha(char):
    return ord(char)-97 # "a" start from 97
while(True):
    key=3 # in cieser
    alpha = list(string.ascii_lowercase) #[a,b,c,d,....z]
    plain_text= list(map(n_alpha,input("Please enter the plain text(or c to cancel): \n").lower().replace(" ", ""))) #convert apha into numeric
    if plain_text==[2]:
            sys.exit("thank you for using my program for encryption")
    cipher_text= []
    for i in plain_text:
        if (i>=0) and (i<=25-key): #alpha 
            cipher_text.append(alpha[i+key]) #cieser shift (convert numeric into alpha)
        elif i>25-key:
            cipher_text.append(alpha[(i%26+key)%26])
        else:
            print("invalid input please enter a text from a to z")
    print("\nthe cipher is :\n",*cipher_text,sep='')





