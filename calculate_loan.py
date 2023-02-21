def calculate_loan(property_price,loan,interest_rate):
    if property_price*0.7<loan:
        yearly=loan*0.02
        montly=yearly/12
        print("amortization:",montly)
        yearlyInterest=loan*interest_rate
        montlyInterest=yearlyInterest/12
        print("interest:", montlyInterest)
    elif property_price*0.5<loan:
        yearly = loan * 0.01
        montly = yearly / 12
        print("amortization:",montly)
        yearlyInterest = loan * interest_rate/100
        montlyInterest = yearlyInterest / 12
        print("interest:", montlyInterest)
        print("total:",montlyInterest+montly)
    else:
        yearlyInterest = loan * interest_rate/100
        montlyInterest = yearlyInterest / 12
        print("amortization: 0.0")
        print("interest:", montlyInterest)
        print("total:", montlyInterest)

calculate_loan(1800000, 1200000, 1.2)

#→
#amortization: 1000.0
#interest: 1200.0
#total: 2200.0

calculate_loan(1500000, 600000, 1.2)

#→
#amortization: 0.0
#interest: 600.0
#total: 600.0