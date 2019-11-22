"""x = 0
while True:
    x += 1
    if x == 20:
        break
    if x % 2 == 0:
        continue
    print(x)

words = [['s', 'a', 'l', 'a', 'm'], ['k', 'h', 'o', 'o', 'b', 'i', '?'], ['n', 'a']]

for word in words:
    for char in word:
        print(char, end='')
    print()
"""
"""
n = input()
n= int(n)
if( n>= 1 & n<=100):
    for i in range(1 , n+1):
        for j in range(1, n+1):
            print(i*j," ", end='')
        print()
    pass
"""
n, d = map(int, input().split())
if( (n >= 2 and n <= 100) or (d >= 1 and d<=1000)):
    p =0
    i=0
    while True:
        i+=1
        p += d
        r = p % n
        if(r >= 0 and r <= n/2):
            # print(i," ",p)
            print(p)
            break
        pass
    pass