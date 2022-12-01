import string
import sys
import random

text = []

if len(sys.argv)<2:
    print ('-h for help')
    sys.exit()
if "-h" in sys.argv:
    print ('''
 flags:
 -h   help
 -u   uppercase
 -l   lowercase
 -d   digits
 -p   punctuation
 example:
 python pass-gen.py -u -l -d -p 12 
    ''')
    sys.exit()

if "-u" in sys.argv:
    text.append(string.ascii_uppercase)

if "-l" in sys.argv:
    text.append(string.ascii_lowercase)

if "-d" in sys.argv:
    text.append(string.digits)

if "-p" in sys.argv:
    text.append(string.punctuation)

length = sys.argv[-1]
    
text2 = "".join(i for i in text)
print(''.join(random.choices(text2, k=int(length))))