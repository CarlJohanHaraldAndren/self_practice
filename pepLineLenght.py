def pepLineLength(filename):
    file=open(filename)
    text=file.read()
    file.close()
    textList=[]
    textList.append(text.split('\n'))
    lineNr=1
    linesTooLong=0
    for lines in textList:
        for line in lines:
            if len(line)>79:
                print("line",lineNr,"too long:",len(line))
                linesTooLong+=1
            lineNr += 1

    print(linesTooLong, "lines are too long")
    #print(textList)



