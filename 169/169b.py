n = int(input())
a = list(map(int,input().split()))

if 0 in a:
    print(0)
    exit()
ans = 1
for i in a:
    ans *= i
    if ans > 10**18:
        ans = -1
        break
print(ans)
