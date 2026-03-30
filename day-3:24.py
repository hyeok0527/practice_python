def contains(bag, e):
    return e in bag

def insert(bag, e):
    bag.append(e)
    
def remove(bag, e):
    bag.remove(e)
    
def count(bag):
    return len(bag)

mybag = []

insert(mybag, 'cellphone')
print('in my bag:', mybag)
print(contains(mybag,'cellphone'))

import time
mybag = []
start = time.time()
insert(mybag, 'protein')
insert(mybag, 'protein')
insert(mybag, 'protein')
print('in my bag', mybag)
end = time.time()
print("running time = ",end-start)

def search(bag, key):
    n = len(bag)
    for i in range(n):
        if bag[i] == key:
            return i
    return -1

print(search(mybag, 'protein'))
print(search(mybag, 'water'))

def factorial_iter(n):
    result = 1
    for k in range(1,n+1):
        result = result * k
    return result

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial_iter(10))
print(factorial(10))

def hanoi_tower(n, fr, tmp, to) :
    if(n==1):
        print("원판 1: %s --> %s" % (fr, to))
    else:
        hanoi_tower(n-1, fr, to, tmp)
        print("원판 %d: %s --> %s" % (n,fr,to))
        hanoi_tower(n-1,tmp,fr,to)
        
hanoi_tower(4,'A','B','C')

def find_min_max(A) :
    min = A[0]
    max = A[0]
    for i in A:
        if min < i:
            min = i
        if max > i:
            max = i
    print(max,min)
    x = (min, max)
    print( x)

Arr = [ 1, 2, 3, 4, 5, 6, 7]
find_min_max(Arr)
