src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_9_B"


def shuffle(s: str, n: int) -> str:
    f = s[n:]
    b = s[:n]
    return f + b


result = []

while 1:
    s = input()
    if s == "-":
        break
    m = int(input())
    for i in range(m):
        s = shuffle(s, int(input()))
    result.append(s)

for i in result:
    print(i)
