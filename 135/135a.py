a,b = map(int,input().split())
ans = a + b

if ans % 2 == 0:
    print(int(ans / 2))
else:
    print('IMPOSSIBLE')
