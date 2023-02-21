def pandemic_rules(numC, totalNum, population):

    infections=(totalNum/population)*100000
    #the actual number of infections in C (numC)
    #the total number of cases for two weeks (totalNum)
    #the population size in the traveler's country (population)
    if infections>numC:
        if infections>50:
            return 'red'
        elif infections in range(25,50):
            return 'yellow'
        elif infections<25:
            return 'green'
        else:
            return 'red'
    else:
        return 'green'

pandemic_rules(10,350,1000000) #→ 'yellow'	None	FAIL
pandemic_rules(20,2500,5000000) #→ 'red'	None	FAIL
pandemic_rules(10,1500,6500000) #→ 'green'	None	FAIL
pandemic_rules(150,8500,6500000) #→ 'green'