import pyperclip
import random
import string

alphabet = string.printable[0:95]
alphabet = list(alphabet)

def encode(inputstring):
    codedmsg = []
    while True:
        try:
            key = int(input('\nSet a super secret key (Any number): '))
            while key >= len(alphabet):
                key = key // 2
            break
        except:
            continue
    for i in inputstring:
        codedchar = (alphabet.index(i)) + key
        if codedchar >= (len(alphabet)):
            codedchar = codedchar - (len(alphabet))
        codedmsg.append(alphabet[codedchar])
    pyperclip.copy(''.join(codedmsg))
    print('\'' + ''.join(codedmsg) + '\' copied to clipboard.')

def decode(inputstring):
    decodedmsg = []
    while True:
        try:
            key = int(input('\nSet a super secret key (Any number): '))
            while key >= len(alphabet):
                key = key // 2
            break
        except:
            continue
    for i in inputstring:
        decodedchar = (alphabet.index(i)) - key
        if decodedchar < 0:
            decodedchar = decodedchar + (len(alphabet))
        decodedmsg.append(alphabet[decodedchar])
    print(''.join(decodedmsg))

def brute(inputstring):
    decodedmsg = []
    for i in range(len(alphabet)):
        key = i
        for i in inputstring:
            decodedchar = (alphabet.index(i)) - key
            if decodedchar < 0:
                decodedchar = decodedchar + (len(alphabet))
            decodedmsg.append(alphabet[decodedchar])
        print(''.join(decodedmsg))
        decodedmsg = []


        


# RANDOM KEY GENERATOR, cba to implement it though whatever
##key = random.randint(1, (999**3))
##print('Key: ' + str(key))
##while key > 40:
##    key = key // 2

    
    
       
