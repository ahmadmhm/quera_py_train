o = []
m = "MOLANA"
h = "HAFEZ"
for i in range(0, 5):
    text = input()
    m1 = text.find(m)
    h1 = text.find(h)
    if m1 > -1 or h1 > -1:
        o.append(i+1)
    pass
if len(o) == 0:
    print("NOT FOUND!")
for i in o:
    print(i, end=' ')
    pass
