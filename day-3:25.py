mySet = set([12, 33, 52, 26, 99])           #set 집합 지정
for e in mySet :
    print("값 =",e)
    
mydict = { 'A':12, 'B':33, 'C':52, 'D':26, 'E':99, }
for e in mydict :
    print("key = ",e)
    print("value = ",mydict[e])
    
def sum_range(begin,end,step =1):
    sum = 0
    for n in range(begin, end, step):
        sum += n
    return sum

print(sum_range(1,10))

import min_max

data = [ 5, 3, 8, 4, 9, 1, 6, 2 ,7 ]
print(min_max.find_min_max(data))