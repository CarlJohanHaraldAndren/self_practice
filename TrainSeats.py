class TrainSeats:
    def __init__(self, nrOfSeats):
        self.nrOfSeats = nrOfSeats
        self.seats=[]
        self.booked=[]

    def pick(self, seatNum):
        if seatNum in self.seats:
            return False
        else:
            self.seats.append(seatNum)
            return True

    def book(self, n):
        if n+len(self.seats)>self.nrOfSeats:
            return None
        else:
            i=0
            j=0
            while i in range(n):
                if j not in self.seats:
                    self.booked.append(j)
                    i+=1
                    j+=1
                else:
                    j+=1

            return self.booked



def case1():
    seats = TrainSeats(10)
    return seats.pick(0)

# → True

def case2():
    seats = TrainSeats(10)
    return seats.pick(9)

# → True

def case3():
    seats = TrainSeats(10)
    seats.pick(1)
    return seats.pick(1)

# → False

def case4():
    seats = TrainSeats(10)
    seats.pick(3)
    return seats.book(5)

# → [0, 1, 2, 4, 5]

def case5():
    seats = TrainSeats(10)
    return seats.book(50)

# → None

print(case1())
print(case2())
print(case3())
print(case4())
print(case5())