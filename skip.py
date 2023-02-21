def skip(n,list):
    tomLista=[0]
    if n==1:
        tomLista=list
        return tomLista
    elif len(list)==n:
        tomLista[0]=list[0]
        return tomLista
    elif list:
        lenghtLista=int((len(list)/n)+1)
        tomLista=[0 for i in range(lenghtLista)]
        for i in range(lenghtLista):
            tomLista[i]=list[i*n]
        return tomLista
    else:
        return tomLista

print(skip(5,['A','B','C','D','E']) )
