# ## Decryption

import string
import sys

def n_alpha(char):
    return ord(char)-97 # "a" start from 97

key=3 # in cieser
alpha = list(string.ascii_lowercase) #[a,b,c,d,....z]
cipher_text= list(map(n_alpha,input("Please enter the Cipher text (or c to cancel): \n").lower().replace(" ", ""))) #convert apha into numeric
plain_text = []
for i in cipher_text:
    if (i>=0) and (i<=25-key): #alpha 
        plain_text.append(alpha[i-key]) #cieser shift (convert numeric into alpha)
    elif i>25-key:
        plain_text.append(alpha[(i%26-key)%26])
    else:
        print("invalid input please enter a text from a to z")
print("\nthe plain text is :\n",*plain_text,sep='')

