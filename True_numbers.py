import re
def check_number(number):
    s1 = re.findall("([-+]?[0-9]*\.?[0-9]+[eE][-+]?[0-9]+)", number)
    if s1:
        print("s1 ",s1[0])
        if len(number) - number.count(" ") == len(s1[0]) - s1[0].count(" "):
            return "LEGAL"
        else:
            return "ILLEGAL"
    else:
        s2 = re.findall("(\s*[+-]?[0-9]+[.][0-9]+\s*)", number)
        if s2:
            if number.count("+") >1 or number.count("-") >1 or number.count(".") >1:
                return "ILLEGAL"
            print("s2")
            return "LEGAL"
        else:
            s3 = re.findall("(\s*[0-9]+\s*)", number)
            if number.find(".") > -1 or number.find("e") > -1:
                return "ILLEGAL"
            if s3:
                if number.count("+") > 1 or number.count("-") > 1:
                    return "ILLEGAL"
                print("s3")
                return "LEGAL"
            else:
                return "ILLEGAL"
    pass
# [-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)
inputs = []
try:
    # while True:
        line = input()
        print(check_number(line))
        # inputs.append(check_number(line))
except:
    for result in inputs:
        print(result)
    pass