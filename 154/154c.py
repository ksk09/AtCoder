N = int(input())
A = list(map(int, input().split()))

ans = set(A)
l = len(ans)
if(N == l):
    print('YES')
else:
    print('NO')
