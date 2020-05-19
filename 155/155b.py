N = int(input())

A = list(map(int,input().split()))

flg = 1
for i in range(N):
    if (A[i] % 2 == 0):
        if(A[i] % 3 == 0 or A[i] % 5 == 0):
            flg = 1
        else:
            flg = 0
            break

if(flg == 1):
    print('APPROVED')
else:
    print('DENIED')
        
