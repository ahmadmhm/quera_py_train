
x , y = map(float, input().split())
#Cr(x,y)
x = int(x)
y = int(y)
def comb(x,y):
    if x < y:
        return 0
        pass
    elif y == 0 or x == y :
        return 1
        pass
    elif x - y == 1 :
        return x
        pass
    elif x - y == 1 :
        return x
        pass
    else:
        xf = 1
        yf = 1
        xyf = 1
        for i in range(2, x+1):
            xf *= i
            pass
        for i in range(2, y+1):
            yf *= i
            pass
        for i in range(2, x-y+1):
            xyf *= i
            pass
        # return xf/(xyf*yf)
        print (xf/(xyf*yf))
    pass


comb(x,y)