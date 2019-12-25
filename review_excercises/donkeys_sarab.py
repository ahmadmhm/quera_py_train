n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if x == 1 and y == 1:
       print("1")
    elif x == 1 and y == 0:
           print("-1")
    elif x % 2 == 0:
        if y == x -2:
            print(2 * x - 2)
        elif y == x:
            print(2 * x)
        else:
            print("-1")
        pass
    elif x % 2 == 1:
        if y == x -2:
            print(2 * x - 3)
        elif y == x:
            print(2 * x - 1)
        else:
            print("-1")
        pass
    else:
        print("-1")
    pass