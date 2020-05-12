import numpy as np
N, M = map(int, input().split())

A = list(map(int, input().split()))
         
n = N - np.sum(A)
if(n >= 0):
    print(n)
else:
    print(-1)
