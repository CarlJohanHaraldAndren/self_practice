class SimpleCounter:
    def __init__(self):
        self.countNu = 9999

    def count(self):
        self.countNu += 1

    def reset(self):
        self.countNu = 0

    def getValue(self):
        return self.countNu


class BoundedCounter(SimpleCounter):
    def __init__(self, init, max):
        super().__init__()
        self.init = init
        self.countNu = self.init
        self.max = max

    def count(self):
        if self.countNu < self.max:
            self.countNu += 1
        else:
            self.countNu = 0


class ChainedCounter(BoundedCounter):
    def __init__(self, init, max, next):
        super().__init__(init, max)
        self.init = init
        self.max = max
        self.next = next

    def count(self):
        if self.countNu < self.max:
            self.countNu += 1
        else:
            self.countNu = 0
            if self.next:
                self.next.count()



def case1():
    return SimpleCounter().getValue()


def case2():
    c = SimpleCounter()
    c.reset()
    return c.getValue()


def case3():
    c = SimpleCounter()
    c.reset()
    c.count()
    return c.getValue()


def case4():
    c = BoundedCounter(9999, 9999)
    c.count()
    return c.getValue()


def case5():
    h = ChainedCounter(11, 24, None)
    m = ChainedCounter(59, 59, h)
    m.count()
    return (h.getValue(), m.getValue())


def case6():
    c = ChainedCounter(10, 10, None)
    c.count()
    return c.getValue()


print(case1())
print(case2())
print(case3())
print(case4())
print(case5())
print(case6())
