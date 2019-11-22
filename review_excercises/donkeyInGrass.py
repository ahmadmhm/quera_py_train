x, y, z = map(int, input().split())

if z % 2 == 0:
    print(int(z / 2) * x + int(z / 2) * y)
else:
    print(int((z / 2)+1) * x + int(z / 2) * y)
    pass