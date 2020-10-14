src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_D"

# ---- solution ----
land = input()
hs, ls, area = [], [], 0

for i in range(len(land)):
    if land[i] == "\\":
        hs.append(i)
    elif land[i] == "/" and hs:
        j = hs.pop()
        a = i - j
        area += a

        while ls and ls[-1][0] > j:
            a += ls.pop()[1]
        ls.append([j, a])

print(area)
print(len(ls), *(a for j, a in ls))
