A, B, C = map(int, input().split())

list = [A,B,C]

a = set(list)

if(len(a) == 2):
    print('Yes')
else:
    print('No')
