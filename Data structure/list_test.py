a = [10, 20, 30]
print(a)
b = a
print(b)
a[1]+=1
print(b)
myList = [10, 20, 30]
myList.append(40)
print(myList)
myList.extend([50, 60])
print(myList)
myList.insert(1, 15)
print(myList)

myList = ['ali', 1, 2, 3, 'chetor']
for i, it in enumerate(myList):
  print("the {0}th object in myList is {1}!".format(i+1, it))
listA = [1, 2, 3, 4]
listB = ['a', 'b', 'c', 'd']
listC = ['I', 'II', 'III', 'IV']
for a, b, c in zip(listA, listB, listC):
    print("{0}th alphabet or {1} in greece is {2}".format(a, c, b))
sq = [x*x for x in range(10)]
print(sq)
sq1 = [str(x)+str(y) for x in [1, 2, 3] for y in ['A', 'B']]
print(sq1)
sq2 = [(x, y) for x in [1, 2, 3] for y in [1, 2, 3] if x != y]
print(sq2)
data = [10, -4, 53, 122, 0]
d1 = [x for x in data if x > 0]
d2 = [x*x for x in data]
matrix = [[j+i*3+1 for j in range(3)] for i in range(3)]
a = ['ali', 'rafte', 'key', 'barmigarde?']
del a[0]
print(a)
del a[0:2]
print(a)

def f(a, *args):
    return args
    pass
print(f(1, 2, 3))

def f(*args, **kwargs):
    print(args)
    print(kwargs)
    pass
print(f(1, a=2))
