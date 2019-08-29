users =[]
albums=[]

n = int(input())
m=0
for i in range(n):
    user = {}
    user['name'] = input().rsplit(' ', 1)[1]
    user['age'] = int(input().rsplit(' ', 1)[1])
    user['city'] = input().rsplit(' ', 1)[1]
    alb = input()
    tmp1 ='0'
    while True:
        tmp = []
        alb = input()
        print(alb.split(' ', 1))
        if alb.split(' ', 1)[0] == '':
            tmp.append(alb.rsplit(' ', 1)[1])
        else:
            if i == n-1:
                m = alb
                pass
            elif alb.split(' ', 1)[0] == '-':
                break
        pass

    user['albums'] = tmp
    users.append(user)
    pass
print(users)
print(m)
# m = int(input())
# for i in range(m):
#     album = {}
#     album['name'] = input().rsplit(' ', 1)[1]
#     album['singer'] = input().rsplit(' ', 1)[1]
#     album['genre'] = input().rsplit(' ', 1)[1]
#     album['tracks'] = int(input().rsplit(' ', 1)[1])
#     albums.append(album)
#     pass
# print(albums)