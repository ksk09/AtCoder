n = int(input())

s,t = map(str,input().split())

ans = ''
for i in range(n):
    ans += s[i] + t[i]

print(ans)
