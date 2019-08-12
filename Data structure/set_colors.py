k = int(input())
s= {}

for i in range(0, k):
    name, fm = map(str, input().split())
    if name in s:
        s[name] +=1
        pass
    else:
        s[name] =1
    pass
sn = sorted(s.items(), key=lambda x: x[1], reverse=True)
print(sn[0][1])