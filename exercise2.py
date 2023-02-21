import binaryconv as bc

# 1. ---------------------------------------------
# Complete the function invisible2bin which takes a
# string of spaces and tabs and returns a new string
# where every space is replaced with 0 and every tab
# character is replaced with 1.


def txt2bin(txt):
    bin = []
    for c in txt:
        bin.append(bc.padzero(bc.dec2bin(ord(c)),8))
    return "".join(bin)

def bin2invisible(bin):
    inv = []
    for b in bin:
        if b=='0':
            inv.append(' ')
        else:
            inv.append('	')
    return "".join(inv)

def txt2invisible(txt):
    return bin2invisible(txt2bin(txt))

def invisible2bin(inv):
    bin=[]
    for b in inv:
        if b == ' ':
            bin.append('0')
        else:
            bin.append('1')
    return "".join(bin)

# 2. ---------------------------------------------
# Complete the function bin2txt which takes a string
# of 0 and 1 and converts it to text. This can be done
# by chunking the binary string into chunks of eight
# binary digits and passing each chunk to the function
# bin2dec defined in the module binaryconv. bin2dec takes a
# sequence of binary digits and converts that into a number.
# The only thing left is to call the standard function chr
# which will convert the number into a character. Concatenate
# all characters into a string to get the final result.

#bin='01011010'

def bin2txt(bin):
    result=[]
    for i in range(int(len(bin)/8)):
        if i == 0:
            result.append(chr(bc.bin2dec(bin[0:8])))
        elif i == 1:
            result.append(chr(bc.bin2dec(bin[8:16])))
        elif i== 2:
            result.append(chr(bc.bin2dec(bin[16:24])))

    return "".join(result)



def invisible2txt(inv):
    return bin2txt(invisible2bin(inv))