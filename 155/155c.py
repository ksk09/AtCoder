from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
 
count = Counter(s)
maxNum = max(count.values())
t = sorted(list(set(s)))
for i in t:
  if count[i] == maxNum:
    print(i)
