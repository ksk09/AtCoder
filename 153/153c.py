N, K = map(int, input().split())

H = list(map(int, input().split()))

if(K >= N):
    print(0)
else:
    H.sort()
    h = H[:N-K]
    print(sum(h))
