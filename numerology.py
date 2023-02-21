
def numeric_value(string):
    string=string.lower()
    value=0
    for i in range(0,len(string)):
        value+=ord(string[i])-96
        print(value)
    return value

print(ord('e'))
#print(len('Alice'))
print(numeric_value('Alice'))