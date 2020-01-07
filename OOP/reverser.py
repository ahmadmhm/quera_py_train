class Reverse:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if(len(self.data) == 0):
            raise StopIteration
        index = len(self.data)
        # print(self.data[len(self.data)-1])
        return self.data.pop(index-1)
    pass


ls = [10, 20, 30]
f = Reverse(list(ls))
# print(f)
for it in f:
    print(it)
print(ls)

# s = "salam,khoobi?!"
# a = Reverse(list(s))
#
# for char in Reverse(list(s)):
#     print(char, end='')