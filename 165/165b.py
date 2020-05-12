X=int(input())
yen = 100
c = 0

while yen < X:
    d = yen // 100
    yen += d
    c  += 1
print(c)
