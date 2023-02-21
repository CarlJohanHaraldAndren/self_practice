def swap(list):
    halva=int(len(list)/2)
    newList=[0 for i in range(len(list))]
    newList[0:halva]=list[halva:]
    newList[halva:]=list[0:halva]
    return newList

print(swap([1,2,3,4]))