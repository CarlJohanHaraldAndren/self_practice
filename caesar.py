# Implement the cipher as a function, i.e. caesar(2,'secret')
# should return 'ugetgv'. Make sure that when you shift the
# letters in the alphabet, you also wrap around. One way to
# do that is that when you compute the index of the shifted
# letter, you also check whether the index is negative or
# bigger than 25. Another way is to use modulus 26 (e.g. % 26 in Python).

def caesar(a,string):
    newString=[]
    for line in string:
        if (ord(line)+a) < 96:
            # 99-4 = 95
            # 120
            newString.append(chr(((ord(line) + a) - 96) + 122))

        elif (ord(line)+a) < 122:
            newString.append(chr(ord(line) + a))
        else:
            newString.append(chr(((ord(line)+a)-122)+96))

    return "".join(newString)

print(caesar(2,'secret'))
print(caesar(4,'yield') ) #'cmiph'
print(caesar(-5,'ltqi'))
print(caesar(-4,'cmiph')) #yield