# src = https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_7_C

r, c = map(int, input().split())
table = []
for i in range(r):
    table.append(list(map(int, input().split())))

table.append([])

for i in range(c):
    sc = 0
    for j in range(r):
        sc += table[j][i]
    table[-1].append(sc)

for i in range(r + 1):
    table[i].append(sum(table[i]))

for row in table:
    print(*row)
