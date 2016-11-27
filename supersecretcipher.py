import pyperclip
import random
alphabet = (r'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.!? ')
alphabet = list(alphabet)
key = 5
codedmsg = []
decodedmsg = []

def encode(inputstring):
    for i in inputstring:
        codedchar = (alphabet.index(i)) + key
        if codedchar > (len(alphabet) - 1):
            codedchar = codedchar - (len(alphabet))
        codedmsg.append(alphabet[codedchar])
    pyperclip.copy(''.join(codedmsg))
    print('\'' + ''.join(codedmsg) + '\' copied to clipboard.')

def decode(codedmsg):
    for i in codedmsg:
        decodedchar = (alphabet.index(i)) - key
        if decodedchar < 0:
            decodedchar = decodedchar + (len(alphabet))
        decodedmsg.append(alphabet[decodedchar])
    print(''.join(decodedmsg))

while True:
    while True:
        try:
            key = int(input('\nSet a super secret key (Any number): '))
            while key > 40:
                key = key // 2
            break
        except:
            continue
        
    inputstring = input('Message: ')
    inputstring = list(inputstring)
    encode(inputstring)
    decode(codedmsg)
    codedmsg = []
    decodedmsg = []


# RANDOM KEY GENERATOR, cba to implement it though whatever
##key = random.randint(1, (999**3))
##print('Key: ' + str(key))
##while key > 40:
##    key = key // 2

    
    
       
