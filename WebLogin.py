class User:
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def getName(self): return self.name

    def getPassword(self): return self.password

    def sendMessage(self, message): print(message, "sent to", self.email)

class WebLogin:

    def __init__(self, name=None, password=None, email=None):
        self.name = name
        self.password = password
        self.email = email
        self.users = {}

    def addUser(self, name, password, email):
        self.users[name] = (password, email)
        print(self.users)

    def login(self, name, password):
        if name in self.users and password in self.users.get(name):
            return True
        else:
            return False

    def sendPassword(self, name):
        if name in self.users:
            print("Your password is:",self.users.get(name)[0], "sent to", self.users.get(name)[1])
        else:
            return False






def case1():
    wl = WebLogin()
    wl.addUser('Alice', '123', 'alice@example.com')
    wl.addUser('Bob', '456', 'bob@example.com')
    return wl.login('Bob','456')

#True
print(case1())

def case2():
    wl = WebLogin()
    wl.addUser('John', 'x26', 'john@example.com')
    wl.addUser('Mary', '666', 'mary@example.com')
    return wl.login('John','x27')
print(case2())
#False

def case3():
    wl = WebLogin()
    wl.addUser('Alexa', '123', 'alexa@example.com')
    wl.addUser('Robin', '456', 'robin@example.com')
    return wl.login('Alice','123')

print(case3())
#False

def case4():
    wl = WebLogin()
    wl.addUser('Alice', '123', 'alice@example.com')
    wl.addUser('Bob', '456', 'bob@example.com')
    wl.sendPassword('Bob')

print(case4())
#Your password is: 456 sent to bob@example.com
