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
n = input()
n= int(n)
if( n>= 1 & n<=100):
    for i in range(1 , n+1):
        for j in range(1, n+1):
            print(i*j," ", end='')
        print()
    pass