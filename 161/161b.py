N, M = map(int, input().split())
A = list(map(int,input().split()))
B = 0

for i in range(N):
    if (A[i] >= sum(A) / (4*M)):
        B +=1

if B >= M:
    print('Yes')
else:
    print('No')


