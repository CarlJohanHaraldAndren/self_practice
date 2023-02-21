def code_words(text, dictionary):
    textList=text.split()
    #print(textList)
    i=0
    for ord in textList:
        #print(ord)
        if ord in dictionary:
            #print("yo")
            textList[i]=dictionary[ord]
        i += 1
    return ' '.join(textList)


#dict={'happiness': 'cake', 'homework': 'date'}
#print(dict['happiness'])

code_words('you have your happiness',{'happiness': 'cake', 'homework': 'date'})
#→ 'you have your cake'	None	FAIL
code_words('I have a homework today',{'happiness': 'cake', 'homework': 'date'})
#→ 'I have a date today'	None	FAIL
code_words('where is the cabbage',{'cabbage': 'money'})
#→ 'where is the money'	None