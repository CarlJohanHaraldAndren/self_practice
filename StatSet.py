class StatSet:
    def __init__(self):
        self.set=[]

    def addNumber(self,x):
        self.set.append(x)

    def mean(self):
        sum=0
        for i in range(len(self.set)):
            sum+=self.set[i]
        return sum/len(self.set)

    def median(self):
        return (max(self.set)+min(self.set))/2

    def stdDev2(self):
        n=len(self.set)
        s2=0
        s=0
        for i in range(n):
            s2+=self.set[i]**2
            s+=self.set[i]
        s=s2/n-(s/n)**2
        return s


    def count(self):
        return len(self.set)

    def min(self):
        return min(self.set)

    def max(self):
        return max(self.set)

def case1():
    set = StatSet()
    set.addNumber(10)
    set.addNumber(20)
    set.addNumber(30)
    return set.mean()


# → 20

def case2():
    set = StatSet()
    set.addNumber(10)
    set.addNumber(20)
    set.addNumber(50)
    return (set.min(),set.median(),set.max())

# → (10, 30, 50)

def case3():
    set = StatSet()
    set.addNumber(1)
    set.addNumber(2)
    return set.count()

# → 2

def case4():
    set = StatSet()
    set.addNumber(-1)
    set.addNumber(0)
    set.addNumber(1)
    set.addNumber(2)
    set.addNumber(3)
    return (set.mean(),set.stdDev2())

# → (1, 2)