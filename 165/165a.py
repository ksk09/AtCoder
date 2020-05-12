K=int(input())

A, B=map(int, input().split())

d = A // K
while 1:
    s = K * d
    if(s >= A and s <= B):
        print('OK')
        break
    elif(s > B):
        print('NG')
        break
    else:
        d += 1
    
