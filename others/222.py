import sys
from math import floor

h, a, b = map(int, input().split())

s = a - b
if(s <= 0):
    print('NO')
else:
    ans = floor(h / s)
    print('YES')
    print(ans)

      
