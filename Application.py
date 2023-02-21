class Application:
    def __init__(self, name, personalNum, distance):
        self.name = name
        self.personalNum = personalNum
        self.distance = distance

    def getName(self): return self.name

    def getPersonalNumber(self): return self.personalNum

    def distanceFromSchool(self): return self.distance

# AttributeError: 'ApplicationList'
# object has no attribute 'printAccepted' on line 29

class ApplicationList:
    def __init__(self, nrOfStudents):
        self.nrOfStudents = nrOfStudents
        self.studentList = [] # tuple istället

    def addApplication(self, app):
        # addApplication(Application('Erik','123',2))
        if Application.distanceFromSchool(app) <= 5:
            self.studentList.append((Application.getName(app), Application.getPersonalNumber(app), Application.distanceFromSchool(app)))
        return self.studentList


    def printAccepted(self):
        #print(self.studentList[:self.nrOfStudents])
        self.studentList=self.studentList[:self.nrOfStudents]
        for i in range(len(self.studentList)):
            print(self.studentList[i][0], self.studentList[i][1])
        #print(sorted(self.studentList, key=lambda x: x[1])[:self.nrOfStudents])


def case1():
    list = ApplicationList(2)
    list.addApplication(Application('Erik','123',2))
    list.addApplication(Application('Maria','322',1.5))
    list.addApplication(Application('Stefan','311',0.5))
    list.printAccepted()


# →
# Erik 123
# Maria 322

def case2():
    list = ApplicationList(2)
    list.addApplication(Application('Erik','123',2))
    list.addApplication(Application('Maria','322',10))
    list.addApplication(Application('Stefan','311',0.5))
    list.addApplication(Application('Eva','811',1))
    list.printAccepted()

# →
# Erik 123
# Stefan 311
print("case 1")
case1()
print("case 2")
case2()