users =[]
albums=[]

n = int(input())
m=0
tmp1 = '0'
for i in range(n):

    user = {}
    if tmp1 == '0':
        user['name'] = input().rsplit(' ', 1)[1]
    else:
        user['name'] = tmp1
        tmp1 = '0'
    user['age'] = int(input().rsplit(' ', 1)[1])
    user['city'] = input().rsplit(' ', 1)[1]
    alb = input()
    tmp = []

    while True:
        alb = input()
        # print(alb.split(' ', 1))
        if alb.split(' ', 1)[0] == '':
            tmp.append(alb.rsplit(' ', 1)[1])
        else:
            if i == n-1:
                m = int(alb)
                break
                pass
            elif alb.split(' ', 1)[0] == '-':
                tmp1 = alb.rsplit(' ', 1)[1]
                break
        pass
    user['albums'] = tmp
    users.append(user)
    if m != 0:
        break
    pass

# print(m)
# m = int(input())
for i in range(m):
    album = {}
    album['name'] = input().rsplit(' ', 1)[1]
    album['singer'] = input().rsplit(' ', 1)[1]
    album['genre'] = input().rsplit(' ', 1)[1]
    album['tracks'] = int(input().rsplit(' ', 1)[1])
    albums.append(album)
    pass
# print(albums)
# print(users)
def one(name ,singer):
    s = 0
    for user in users:
        if user['name'] == name:
            for album in albums:
                if album['name'] in user['albums'] and album['singer'] == singer:
                    s += album['tracks']
                pass
    return s
    pass
def two(name ,genre):
    s = 0
    for user in users:
        if user['name'] == name:
            for album in albums:
                if album['name'] in user['albums'] and album['genre'] == genre:
                    s += album['tracks']
                pass
    return s
    pass
def three(age ,singer):
    s = 0
    for user in users:
        if user['age'] == int(age):
            for album in albums:
                if album['name'] in user['albums'] and album['singer'] == singer:
                    s += album['tracks']
                pass
    return s
    pass
def four(age ,genre):
    s = 0
    for user in users:
        if user['age'] == int(age):
            for album in albums:
                if album['name'] in user['albums'] and album['genre'] == genre:
                    s += album['tracks']
                pass
    return s
    pass
def five(city ,singer):
    s = 0
    for user in users:
        if user['city'] == city:
            for album in albums:
                if album['name'] in user['albums'] and album['singer'] == singer:
                    s += album['tracks']
                pass
    return s
    pass
def six(city ,genre):
    s = 0
    for user in users:
        if user['city'] == city:
            for album in albums:
                if album['name'] in user['albums'] and album['genre'] == genre:
                    s += album['tracks']
                pass
    return s
    pass
m = int(input())
answer = []
for i in range(m):
    temp = input().split(' ')
    if temp[0] == '1':
        answer.append(one(temp[1], temp[2]))
    elif temp[0] == '2':
        answer.append(two(temp[1], temp[2]))
    elif temp[0] == '3':
        answer.append(three(temp[1], temp[2]))
    elif temp[0] == '4':
        answer.append(four(temp[1], temp[2]))
    elif temp[0] == '5':
        answer.append(five(temp[1], temp[2]))
    elif temp[0] == '6':
        answer.append(six(temp[1], temp[2]))
        pass
    # print(temp)
    pass
for item in answer:
    print(item, end='')
    print()
    pass