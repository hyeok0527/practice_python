def find_min_max(A) :
    min = A[0]
    max = A[0]
    for i in A:
        if min < i:
            min = i
        if max > i:
            max = i
    x = (min, max)
    print(x)