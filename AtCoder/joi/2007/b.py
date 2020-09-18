sub = list()
for i in range(28):
    sub.append(int(input()))
for i in range(1, 31):
    if i not in sub:
        print(i)
