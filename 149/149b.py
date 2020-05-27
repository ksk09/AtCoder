a, b, k = map(int, input().split())


if(a>=k):
    a -= k
elif(a>k and k <= a+b):
        sa = abs(a-k)
        a = 0
        b -= sa
else:
    sa = abs(a-k)
    a = 0
    b -= sa
    if b < 0:
        b = 0
print(a, b)
