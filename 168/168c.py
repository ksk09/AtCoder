import math
A, B, H, M = map(int, input().split())

l = 6 * M

s =(H * 60 + M) * 360 / (12 * 60)

abs = abs(l - s)
pi = math.radians(abs)
ans = (A*A + B*B) - (2 * A * B) * math.cos(pi)
print(math.sqrt(ans))
