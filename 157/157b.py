
A = list(list(map(int, input().split())) for i in range(3))
N = int(input())
B = [int(input()) for i in range(N)]
result = [[0]*3 for i in range(3)]

for i in range(3):
    for j in range(3):
        for k in range(N):
            if A[i][j] == B[k]:
                result[i][j] = 1
                break
            else:
                result[i][j] = 0

if (result[0][0]==1 and result[0][1]==1 and result[0][2]==1) \
or (result[1][0]==1 and result[1][1]==1 and result[1][2]==1) \
or (result[2][0]==1 and result[2][1]==1 and result[2][2]==1) \
or (result[0][0]==1 and result[1][0]==1 and result[2][0]==1) \
or (result[0][1]==1 and result[1][1]==1 and result[2][1]==1) \
or (result[0][2]==1 and result[1][2]==1 and result[2][2]==1) \
or (result[0][0]==1 and result[1][1]==1 and result[2][2]==1) \
or (result[0][2]==1 and result[1][1]==1 and result[2][0]==1) :
    print('Yes')
else:
    print('No')
