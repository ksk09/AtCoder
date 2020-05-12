N, K =  map(int, input().split())
         
snukes = [0 for i in range(N)]

for i in range(K):
    d = input()
    A = map(int, input().split())
    for a in A:
        snukes[a - 1] += 1

print(snukes.count(0))
