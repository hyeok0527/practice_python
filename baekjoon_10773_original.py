class stake:
    def __init__ (self, item):
        self.array = []
        self.size = 0
        self.cur = 0
    
    def pus(self, item):
        self.array.append(self.item) = item
        self.size += 1
        self.cur += 1
        
    def out(self):
        if not self.size == 0:
            self.array[self.cur-1] = 0
            self.size -= 1
            self.cur -= 1

a = stake
for i in range(0,int(input())):
    e = int(input())
    if not e == 0:
        a.pus(e)
    else:
        a.out()
        
sum = 0 
for i in a:
    sum += i

print(sum)
