import numpy as np
N = int(input())

A = list(map(int, input().split()))
         
c = [0 for i in range(N)]

for i in range(N-1):
    c[A[i] - 1] += 1

for i in range(N):
    print(c[i])
