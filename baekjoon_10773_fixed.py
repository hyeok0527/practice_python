class Stake:
    def __init__(self):
        self.array = []

    def pus(self, item):
        self.array.append(item)
        
    def out(self):
        if len(self.array) != 0:
            self.array.pop()
a = Stake()

try:
    k = int(input())
    for _ in range(k):
        e = int(input())
        if e != 0:
            a.pus(e)
        else:
            a.out()
            
    print(sum(a.array))
except EOFError:
    pass
except ValueError:
    print("숫자를 입력해주세요.")
