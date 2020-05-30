N = int(input())
S = input()
l = len(S)
ans = ''
for i in S:
    num = ord(i)
    num += N
    if num > 90:
        num = 65 + num % 90 -1
    ans += chr(num)
print(ans)
