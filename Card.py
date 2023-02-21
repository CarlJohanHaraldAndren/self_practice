class Card:
    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit

    #Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King

    def getRank(self): return self.rank

    def getSuit(self): return self.suit

    def value(self):
        if self.rank == 1:
            return 1
        elif self.rank in range(11,13):
            return 10
        else:
            return self.rank

    def __str__(self):
        c = ["Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King"]
        cards = c[0].split(', ')
        cardsList = [[card] for card in cards]

        s = {"d":"Diamonds","c":"Clubs","h":"Hearts","s":"Spades"}

        ut=cardsList[self.rank-1][0] + " of " + s[self.suit]
        return ut





def case1():
    c = Card(1,'s')
    return (c.getRank(),c.value())

# → (1, 1)

def case2():
    c = Card(5,'d')
    return (c.getRank(),c.value())

# → (5, 5)
# (5, 10)	FAIL

def case3():
    c = Card(12,'d')
    return (c.getRank(),c.value())

# → (12, 10)	(12, 10)	OK

def case4():
    c = Card(12,'d')
    return c.getSuit()

# → 'd'	'd'	OK

def case5():
    return str(Card(1,'s'))

# → 'Ace of Spades'	'True'	FAIL

def case6():
    return str(Card(13,'d'))

# → 'King of Diamonds'

print(case1())
print(case2())
print(case3())
print(case4())
print(case5())
print(case6())
