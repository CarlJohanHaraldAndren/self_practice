def movieTickets(nrTickets, nrUnder18, time):
    if time > 18:
        return (nrUnder18*50)+(nrTickets-nrUnder18)*100
    else:
        return ((nrUnder18 * 50) + (nrTickets - nrUnder18) * 100)*0.9


movieTickets(5,3,17) # → 315
movieTickets(0,0,10) # → 0
movieTickets(10,0,20) # → 1000
movieTickets(10,10,20) # → 500
movieTickets(10,5,16) # → 675