n = int(input())
f1=1
f2=2
f=0
for i in range(1, n+1):
    if i == 1:
        print('+', end='')
    elif i == 2:
        print('+', end='')
    elif i == f1 + f2:
        print('+', end='')
        f = f1 + f2
        f1 = f2
        f2 = f
    else:
        print('-', end='')
    pass