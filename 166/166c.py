import numpy as np
N, M =  map(int, input().split())


high = list(map(int, input().split()))
good = [0 for i in range(N)]



for i in range(M):
    A, B =map(int, input().split())
    if (high[A - 1] > high[B - 1]):
        good[B - 1] += 1
    elif (high[A - 1] == high[B - 1]):
        good[A - 1] += 1
        good[B - 1] += 1
    else:
        good[A - 1] += 1

        
print(good.count(0))
