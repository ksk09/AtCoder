import itertools
 
n = int(input())
keep = []
p = tuple((map(int, input().split())))
q = tuple((map(int, input().split())))
for i in range(1, n + 1):
    keep.append(i)
all = list(itertools.permutations(keep))

for j in range(len(all)):
    if all[j] == p:
        ans1 = j
    if all[j] == q:
        ans2 = j
print(abs(ans1 - ans2))
