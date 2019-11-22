number = int(input())
password = input()
wheels = []
movement = 0
#getting the inputs
for i in range(0, number):
    wheels.append(input())
    pass

# print(*wheels, sep = ', ')
# print(wheels[0].find('a'))
def find_direction_count(text , search):
    pos = text.find(search)
    return pos
    pass
#count movements
for j in range(0 , len(password)):
    pos = find_direction_count(wheels[j],password[j])
    if pos != 0:
        if pos <= 4:
            movement += pos
            pass
        elif pos > 4:
            movement += 9 - pos
            pass
        pass
    pass
print(movement)