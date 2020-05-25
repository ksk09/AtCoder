N, K, M = map(int, input().split())

A = list(map(int, input().split()))

s = sum(A)
ave = 0

for i in range(K+1):
    s += i
    ave = s / N
    if(ave >= M):
        print(i)
        break
    elif(i==K):
        print(-1)
    s -= i
