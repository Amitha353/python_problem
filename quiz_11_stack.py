

class superStack:

    def __init__(self):
        super(superStack, self).__init__()
        self.stack = []

    def pushE(self, var):
        self.stack.append(int(var))

    def popE(self):
        var = self.stack[len(self.stack) - 1]
        self.stack.remove(int(var))

    def incByNum(self, num, val):
        for a in range(len(self.stack)):
            print(a)
            if a < int(num):
                self.stack[a] += int(val)

    def detectCommand(self, txt):
        cmd = txt.split(" ")
        if cmd[0] == 'push':
            self.pushE(cmd[1])
        if cmd[0] == 'pop':
            self.popE()
        if cmd[0] == 'inc':
            self.incByNum(cmd[1], cmd[2])
        print(cmd[0])
        print(self.stack)


obj = superStack()
num = int(input())
for a in range(num):
    obj.detectCommand(input())
    print(obj.stack)
    print("")
