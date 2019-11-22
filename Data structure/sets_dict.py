st = {2, 3, 1}
print(st)
a = set("salam")
b = set("ali")

print(a | b)
print(a & b)
print(a - b)
print(a ^ b) # ( A - B) U ( A - B )
print({x for x in a if x not in b})

dict = {"ali": 12, "amir": 2.3}
print(dict['ali'])
print(list(dict))
print({2*x:x/4 for x in range(5)})
d = {'ali': 'A', 'amir': 'B'}
for k, v in d.items():
    print(k + " got " + v)
