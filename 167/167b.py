A, B, C, K = map(int, input().split())


if(K <= A):
    print(K)
else:
    K -= A
    if(K <= B):
        print(A)
    else:
        K -=  B
        print(A - K)
