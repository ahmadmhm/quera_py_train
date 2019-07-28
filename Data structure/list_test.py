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