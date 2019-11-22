def count_without_repeat(text):
    t = ''
    for ch in text:
        if ch not in t:
            t += ch
    return len(t)
    pass

n = int(input())
max = 0
for i in range(0, n):
    text = input()
    result = count_without_repeat(text)
    if result > max:
        max = result
    pass
print(max)
# c = count_without_repeat(text)
# print(c)
