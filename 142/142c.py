n= int(input())
a = list(map(int,input().split()))

print(' '.join(str(i) for a, i in sorted(zip(a, range(1, n + 1)))))
