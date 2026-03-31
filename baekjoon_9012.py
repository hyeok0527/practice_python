import sys

def vps(k):
    sta = []
    for i in k:
        if i == "(":
            sta.append(i)   
        elif i == ")":
            if not sta:
                return "NO"
            sta.pop()
        
    if not sta:        
        return "YES"
    else:
        return "NO"
            
input = sys.stdin.readline
m = int(input())
for i in range(0,m):
    tex = input().strip()
    print(vps(tex))