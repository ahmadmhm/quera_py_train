li = []
inp = 1
while True:
    inp = input()
    if inp != "0":
        li.append(inp)
    else:
        li.reverse()
        for item in li:
            print(item)
        break
    pass