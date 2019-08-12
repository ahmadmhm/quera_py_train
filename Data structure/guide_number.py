# [print(x , end=' ') for x in map(int, input().split())]
# print(*[x for x in [i for i in map(int, input().split())]])


# print([x for x in ([i for i in map(int, input().split())]) ])
print(*sorted(set([x for x,i in zip(list(map(int, input().split())), range(1,200)) if x % 6 == 0 and i % 6 == 0 ])))