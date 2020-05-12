import math
A, B, C, D = map(int,input().split())
hpa = math.ceil(A / D)
hpb = math.ceil(C / B)
if (hpa >= hpb):
    print('Yes')
else:
    print('No')
