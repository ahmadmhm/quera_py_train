import re
def solve(address):
    f = open(address, "r")
    some = 0
    # line = f.readline()
    # if line =='\n':
    #     print("22")
    while True:
        line = f.readline()
        if line != '\n' and line != '':
            if not re.findall("([\s]+\n)", line):
                if not re.findall("(#[a-z0-9]*)", line.strip()):
                    some += 1
                    print(line)
                # print(re.findall("(\s+)", line))
        if line == '':
            break
        pass
    return some
    pass
# print(solve("../functions.py"))
print(solve("f.txt"))