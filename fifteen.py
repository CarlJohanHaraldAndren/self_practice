import random


class FifteenModel:
    def __init__(self):
        # self.puzzle=[[1,2,3,4],
        #             [5,6,7,8],
        #             [9,10,11,12],
        #             [13,14,15,0]]

        self.puzzle = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(4 * i + j + 1)
            self.puzzle.append(row)
        self.puzzle[-1][-1] = 0


    def getValue(self, row, col):
        return self.puzzle[row][col]

    def tryMove(self, row, col):
        if row-1>0 and self.puzzle[row-1][col] == 0:
            self.puzzle[row-1][col]=self.puzzle[row][col]
            self.puzzle[row][col]=0
        elif row+1<4 and self.puzzle[row+1][col] == 0:
            self.puzzle[row+1][col]=self.puzzle[row][col]
            self.puzzle[row][col]=0
        elif col-1>0 and self.puzzle[row][col-1] == 0:
            self.puzzle[row][col-1] = self.puzzle[row][col]
            self.puzzle[row][col] = 0
        elif col+1<4 and self.puzzle[row][col+1] == 0:
            self.puzzle[row][col+1] = self.puzzle[row][col]
            self.puzzle[row][col] = 0
        else:
            pass

    def shuffle(self):
        for i in range(1000):
            self.tryMove(random.randint(0, 3),random.randint(0, 3))

def case1():
    m = FifteenModel()
    return (m.getValue(0, 0), m.getValue(0, 1), m.getValue(0, 2), m.getValue(0, 3)
            , m.getValue(1, 0), m.getValue(1, 1), m.getValue(1, 2), m.getValue(1, 3)
            , m.getValue(2, 0), m.getValue(2, 1), m.getValue(2, 2), m.getValue(2, 3)
            , m.getValue(3, 0), m.getValue(3, 1), m.getValue(3, 2), m.getValue(3, 3))


# → (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

def case2():
    m = FifteenModel()
    m.tryMove(1, 1)  # should not move
    return (m.getValue(0, 0), m.getValue(0, 1), m.getValue(0, 2), m.getValue(0, 3)
            , m.getValue(1, 0), m.getValue(1, 1), m.getValue(1, 2), m.getValue(1, 3)
            , m.getValue(2, 0), m.getValue(2, 1), m.getValue(2, 2), m.getValue(2, 3)
            , m.getValue(3, 0), m.getValue(3, 1), m.getValue(3, 2), m.getValue(3, 3))


# → (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

def case3():
    m = FifteenModel()
    m.tryMove(0, 2)  # corner case
    return (m.getValue(0, 0), m.getValue(0, 1), m.getValue(0, 2), m.getValue(0, 3)
            , m.getValue(1, 0), m.getValue(1, 1), m.getValue(1, 2), m.getValue(1, 3)
            , m.getValue(2, 0), m.getValue(2, 1), m.getValue(2, 2), m.getValue(2, 3)
            , m.getValue(3, 0), m.getValue(3, 1), m.getValue(3, 2), m.getValue(3, 3))


# → (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

def case4():
    m = FifteenModel()
    m.tryMove(3, 2)  # must succeed
    return (m.getValue(0, 0), m.getValue(0, 1), m.getValue(0, 2), m.getValue(0, 3)
            , m.getValue(1, 0), m.getValue(1, 1), m.getValue(1, 2), m.getValue(1, 3)
            , m.getValue(2, 0), m.getValue(2, 1), m.getValue(2, 2), m.getValue(2, 3)
            , m.getValue(3, 0), m.getValue(3, 1), m.getValue(3, 2), m.getValue(3, 3))


# → (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15)

def case5():
    m = FifteenModel()
    m.shuffle()
    return (m.getValue(0, 0), m.getValue(0, 1), m.getValue(0, 2), m.getValue(0, 3)
            , m.getValue(1, 0), m.getValue(1, 1), m.getValue(1, 2), m.getValue(1, 3)
            , m.getValue(2, 0), m.getValue(2, 1), m.getValue(2, 2), m.getValue(2, 3)
            , m.getValue(3, 0), m.getValue(3, 1), m.getValue(3, 2), m.getValue(3, 3)) != (
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)


# → True

print(case1())
print(case2())
print(case3())
print(case4())
print(case5())
