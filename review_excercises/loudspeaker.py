word = input()
text= []
for i in range(0,len(word)):
    text.append(word[i])
    pass
# print("".join(text))
for i in range(0,len(word)):
    for j in range(0 , i+1):
        text[j] = word[i]
        pass
    print("".join(text))
    pass