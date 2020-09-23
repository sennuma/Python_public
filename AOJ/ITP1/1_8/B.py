# src = https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/8/ITP1_8_B

stdins = []
while 1:
    stdin = input()
    if stdin == "0":
        break
    else:
        stdins.append(stdin)

r = []

for stdin in stdins:
    r.append(sum(list(map(int, stdin))))

for i in r:
    print(i)
