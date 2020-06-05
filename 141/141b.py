s = input()

for i, j in enumerate(s):
    if (i + 1) % 2 == 1:
        if j == 'L':
            print('No')
            exit()
    else:
        if j == 'R':
            print('No')
            exit()

print('Yes')
