o = []
n, t = input().split()
n = int(n)
result = 1
ts = set(t)
for i in range(0, n):
    text = input()
    texts = set(text)
    # print(texts)
    for i in texts:
        if i not in ts:
            result = 0
            break
        pass
    # print(result)
    if result == 1:
        for i in ts:
            if i not in texts:
                result = 0
                break
            pass
    if result == 0:
        o.append('No')
    else:
        o.append('Yes')
        pass
    result =1
    pass
# print(len(o))
print(*o , sep="\n")
# for i in o:
#     print(i, end='\n')
"""
n, t = input().split()
lst = []
for i in range(int(n)):
    lst.append(input())
    
for code in lst:
    if set(t) == set(code):
        print('Yes')
    else:
        print('No')
"""