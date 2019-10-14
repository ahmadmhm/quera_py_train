import json
import re
n = int(input())
variables = {}
prints = []
for i in range(n):
    b = input()
    if b.find(':=') > -1:
        name = b.split(":=")[0].replace(" ", "")
        variables[name] = json.loads(b.split(':=')[1].strip())
    else:
        h = re.split(' ', b)[1]
        s = re.search(r"(\[.*?\])", h).group(0).replace('[', '').replace(']', '').replace('"', '').replace('"', '')
        t = re.findall(r"([a-zA-Z0-9]*)", h)[0]

        if isinstance(variables[t], list):
            prints.append(variables[t][int(s)])
            # print(variables[t][int(s)])
        else:
            prints.append(variables[t][s+""])
            # print(variables[t][s+""])
            pass

        # print(s) #inside brackets
        # print(h) #
        # print(t) #variable name
        pass
    pass
for item in prints:
    print(item, end='')
    print()
    pass
# print(isinstance(variables['b'], dict))
