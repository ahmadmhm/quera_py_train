li = []
inp = 1
while True:
    inp = input()
    if inp != "0":
        li.append(inp)
    else:
        li.reverse()
        for i in range(0,len(li)):
            print(li[i])
        break
    pass