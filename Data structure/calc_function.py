def calc(a):
    a = sorted(a)
    #meduim
    med=0.0
    for m in a:
        med += m
        pass
    med /= len(a)
    print(a[int(len(a)/2)-1],"#",a[int(len(a)/2) ])
    if len(a) % 2 == 0:
        mey = (a[int(len(a)/2)-1] + a[int(len(a)/2) ])/2.0
    else:
        mey = a[int(len(a) / 2)]
    return (med, mey, a[len(a)-1])
    pass
print(calc([2, 20, 31]))