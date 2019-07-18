import re
# print(re.findall("e[a-z]", "regex college"))
def check(answer, text):
    text = text.split('#')
    if text[1] == '':
        return answer.find(text[0])
        pass
    elif text[0] == '':
        if int(answer) % pow(10, len(text[1])) == int(text[1]):
            return 1
        else:
            return -1
    elif text[1] != '' and text[0] != '':
        # print(answer[0] == text[0][0])
        if answer.find(text[0]) > -1:
            if answer.find(text[1]):
                if answer[0] == text[0][0]:
                    return 1
                else:
                    return -1
        else:
            return -1
    pass
text = input()
find_sharp = re.findall("([0-9]*#[0-9]*)", text)
# find_number = re.findall("([0-9]+)", "10#1 + 50 = 10052")
all_v = text.split(' ')
if find_sharp[0] == all_v[0]:
    all_v[0] = str(int(all_v[4]) - int(all_v[2]))
    # print(check(all_v[0], find_sharp[0]))
    if check(all_v[0], find_sharp[0]) != -1:
        print(" ".join(all_v))
        # print(check(all_v[0], find_sharp[0]))
        pass
    else:
        print(-1)
        pass
    pass
elif find_sharp[0] == all_v[2]:
    all_v[2] = str(int(all_v[4]) - int(all_v[0]))
    if check(all_v[2], find_sharp[0]) != -1:
        print(" ".join(all_v))
        pass
    else:
        print(-1)
        pass
    pass
elif find_sharp[0] == all_v[4]:
    all_v[4] = str(int(all_v[2]) + int(all_v[0]))
    if check(all_v[4], find_sharp[0]) != -1:
        print(" ".join(all_v))
        pass
    else:
        print(-1)
        pass
    pass
else:

    pass