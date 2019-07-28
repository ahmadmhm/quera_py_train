text = input()
stack = []
for i in range(0,len(text)):
    stack.append(text[i])
    if text[i] == "=":
        stack.pop()
        if stack:
            stack.pop()
    pass
print("".join(stack))