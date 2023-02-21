def div9(num):
    summa=0
    print(str(num))
    if num == 9:
        return summa
    else:
        for i in str(num):
            summa+=int(i)
        div9(summa)
        return summa


div9(1998)

#→
#1998
#27
#9


div9(666666888888888)

#→
#666666888888888
#108
#9