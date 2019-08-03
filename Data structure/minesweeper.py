maps = []
n , m = map(int, input().split())
k = int(input())
def check_bomb(i,j):
    ct = 0
    if i - 1 > -1:
        if j - 1 > -1 and maps[i-1][j-1] == '*':
            ct += 1
        if j + 1 < m and maps[i-1][j+1] == '*':
            ct += 1
        if maps[i-1][j] == '*':
            ct += 1
        pass
    if i +1 < n:
        if j - 1 > -1 and maps[i+1][j-1] == '*':
            ct += 1
        if j + 1 < m and maps[i+1][j+1] == '*':
            ct += 1
        if maps[i+1][j] == '*':
            ct +=1
    if j - 1 > -1 and maps[i][j-1] == '*':
        ct += 1
    if j + 1 < m and maps[i][j+1] == '*':
        ct += 1
    return ct
    pass
for x in range(n):
    maps.append([])
    for y in range(m):
         maps[x].append(0)
         pass
    pass
for i in range(k):
    a, b = map(int, input().split())
    maps[a-1][b-1] = '*'
    pass
for x in range(n):
    for y in range(m):
        if maps[x][y] != '*':
            maps[x][y] = check_bomb(x,y)
        pass
    pass
for x in range(n):
    for y in range(m):
        print(maps[x][y], end=' ')
        pass
    print()
    pass

