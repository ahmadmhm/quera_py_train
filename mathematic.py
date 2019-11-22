import math
x = int(input())
y1 = math.ceil(math.pow(x, 5/3) + math.tan(math.radians(x)))
y2 = math.floor(math.pi * math.pi * math.pow(math.pi, math.atan(math.pow(math.sin(math.radians(x)), 2))))
print(math.gcd(y1, y2))
# print( y2)