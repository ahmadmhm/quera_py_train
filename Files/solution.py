import re
def solve(address):
    f = open(address, "r")
    some = 0

    while True:
        linee = f.readline()
        t = len(linee.strip())
        if linee != '\n' and linee != '':
            if not re.findall("([\s]+\n)", linee) or t > 0:
                if linee.strip() == '#' or not re.findall("(#[.]*)", linee):
                    some += 1
                elif linee.strip().find('#') > 0:
                    some += 1
        # print(t)
        if linee == '':
            break
        pass
    return some
    pass
# print(solve("../functions.py"))
# print(solve("f.txt"))
# print(solve("TEST1.py"))