N = int(input())

S = input()
c =0
for i in range(N-2):
    if(S[i]=='A' and S[i+1]=='B'):
        if(S[i+2]=='C'):
            c += 1
print(c)
        
