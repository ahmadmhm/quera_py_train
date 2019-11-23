r, c = map(int, input().split())
if c > 10:
    print("Left", 10 - r + 1, 21 - c)
elif c <= 10:
    print("Right", 10 - r + 1, c)
pass