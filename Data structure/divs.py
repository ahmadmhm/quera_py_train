def divs(a):
    for i in range(1, a+1):
        if a % i == 0:
            yield i
    pass

for it in divs(10):
    print(it)