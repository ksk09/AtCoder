S = input()

N = len(S)
s = S[::-1]
a = S[:((N-1)//2)]
b = S[((N+3)//2)-1:]
c = a[::-1]
d = b[::-1]

if (S == s and a == c):
    if(b == d):
        print('Yes')
    else:
        print('No')
else:
    print('No')
    
