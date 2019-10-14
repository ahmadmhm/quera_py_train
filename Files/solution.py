import re
def solve(address):
    f = open(address, "r")
    some = 0

    while True:
        line = f.readline()
        if line != '\n' and line != '':
            if not re.findall("([\s]+\n)", line):
                if line.strip() == '#' or not re.findall("(#[.]*)", line):
                    some += 1
                    # print(re.findall("(#[a-zA-Z0-9])", line.strip()))
                elif line.strip().find('#') > 0:
                    some += 1
                    # print(line.strip())

                # print(re.findall("(\s+)", line))
        if line == '':
            break
        pass
    return some
    pass
# print(solve("../functions.py"))
# print(solve("f.txt"))