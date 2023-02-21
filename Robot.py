class Robot:
    def __init__(self):
        self.x=0
        self.y=0
        self.directionIndex=0
        self.directionList=['NORTH','WEST','SOUTH','EAST']

    def getPosition(self):
        return (self.x,self.y)

    def getDirection(self):
        return self.directionList[self.directionIndex]

    def turnLeft(self):
        if self.directionIndex<=3:
            self.directionIndex+=1
        else:
            self.directionIndex=0

    def turnRight(self):
        if self.directionIndex >= 0:
            self.directionIndex -= 1
        else:
            self.directionIndex = 4

    def forward(self,n):
        if self.directionIndex==0:
            self.y+=n
        elif self.directionIndex==1:
            self.x-=n
        elif self.directionIndex==2:
            self.y-=n
        else:
            self.x+=n



def case1():
    robot = Robot()
    robot.forward(10)
    return robot.getPosition()

# → (0, 10)	(0, 0)	FAIL

def case2():
    robot = Robot()
    robot.turnLeft()
    return robot.getDirection()

# → 'WEST'	'NORTH'	FAIL

def case3():
    robot = Robot()
    robot.turnRight()
    return robot.getDirection()

# → 'EAST'	'NORTH'	FAIL

def case4():
    robot = Robot()
    robot.turnRight()
    robot.forward(10)
    return robot.getPosition()

# → (10, 0)	(0, 0)	FAIL

def case5():
    robot = Robot()
    robot.turnRight()
    robot.forward(10)
    robot.turnLeft()
    robot.forward(10)
    return robot.getPosition()

# → (10, 10)