class DiceStats:
    def __init__(self):
        self.rolls = []
        self.frequencies=[0 for i in range(6)] # lol

    def addRoll(self, roll):
        self.rolls.append(roll)
        return roll

    def getFrequences(self):
        for i in range(6):
            self.frequencies[i]=self.rolls.count(i+1)/len(self.rolls)
            # fyller listan frequencies med antalet rolls av
            # nummer 1-6 delat på listans längd
        return self.frequencies

    def isFair(self, epsilon):
        self.getFrequences()
        upper=1/6+epsilon
        lower=1/6-epsilon
        for i in range(6):
            if self.frequencies[i] < upper and self.frequencies[i] > lower:
                return True
            else:
                return False
        #for i in range(6):
        #    if abs(self.frequencies[i] - (1/6+epsilon)) < (1/6+epsilon):
        #        return True
        #    else:
        #        return False

def case1():
    stats = DiceStats()
    stats.addRoll(1)
    stats.addRoll(5)
    stats.addRoll(2)
    stats.addRoll(5)
    return stats.getFrequences()

# → [0.25, 0.25, 0, 0, 0.5, 0]

def case2():
    stats = DiceStats()
    stats.addRoll(1)
    stats.addRoll(4)
    stats.addRoll(6)
    stats.addRoll(3)
    stats.addRoll(5)
    stats.addRoll(2)
    stats.addRoll(6)
    stats.addRoll(1)
    return stats.isFair(0.001)

# → False

def case3():
    stats = DiceStats()
    stats.addRoll(1)
    stats.addRoll(4)
    stats.addRoll(6)
    stats.addRoll(3)
    stats.addRoll(5)
    stats.addRoll(2)
    stats.addRoll(6)
    stats.addRoll(1)
    return stats.isFair(0.09)

# → True

print(case1())
print(case2())
print(case3())