# [백준 10828] 스택 구현하기
# 학습 메모:
# 1. input().split()을 활용해 명령어를 단어 단위로 분리 (인덱스 접근 오류 방지)
# 2. 클래스 메서드 호출 시 괄호()를 반드시 붙여야 함수가 실행됨
# 3. pop 연산 시 size 변수도 함께 관리해주어야 정확한 크기 유지가 가능함
# 4. 클래스 내부 함수 이름과 외부 호출 이름을 일치시켜야 함

class stack:
    def __init__(self):
        self.array = []
        self.size = 0
        
    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0
    
    def pus(self, i):
        self.array.append(i)
        self.size += 1
        
    def po(self):
        if not self.empty():
            self.size -= 1
            return self.array.pop()
        else:
            return -1
    
    def siz(self):
        return self.size
    
    def top(self):
        if not self.empty():
            return self.array[self.size-1]
        else:
            return -1
        
hi = stack()
try:
    k = int(input())
    for i in range(0, k):
        cmd = input().split()

        if cmd[0] == "push":
            hi.pus(int(cmd[1]))
        elif cmd[0] == "pop":
            print(hi.po())
        elif cmd[0] == "size":
            print(hi.siz())
        elif cmd[0] == "empty":
            print(hi.empty())
        elif cmd[0] == "top":
            print(hi.top())
except EOFError:
    pass
