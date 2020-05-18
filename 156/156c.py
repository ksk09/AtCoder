N = int(input())

X = list(map(int, input().split()))

L = min(X)
R = max(X)

ans = 1000000

for i in range(L, R+1):
    tmp = 0
    for j in X:
        tmp += (j - i)**2
    ans = min(ans, tmp)

print(ans)
    
