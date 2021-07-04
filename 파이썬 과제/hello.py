h=int(input())
for i in range(h):
    for j in reversed(range(h)):
        if j>i:
            print(' ',end='')
        elif j==i:
            print('*',end='')
        elif j<i:
            print('*',end='')
    print()
