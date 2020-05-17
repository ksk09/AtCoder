import sys


h, a, b = map(int, input().split())
t = 0

while True:
    t += 1
    h -= a
    if(h <=0):
        print('YES')
        print(t)
        break
    if(b >= a):
        print('NO')
        break
    h += b
