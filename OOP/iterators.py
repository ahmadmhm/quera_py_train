import random

ls = [1, 2, 3, 4]
it = iter(ls)

print(next(it))
print(next(it))

class RandomShuffle:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if(len(self.data) == 0):
            raise StopIteration
        index = random.random() * len(self.data)
        index = int(index)
        return self.data.pop(index)

s = "salam,khoobi?!"

a = RandomShuffle(list(s))

print(s)

for char in a:
    print(char, end='')

print()