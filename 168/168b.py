K = int(input())
S = input()

l = len(S)

if(l <= K):
    print(S)
else:
    s = S[:K]
    print(s + '...')
    
