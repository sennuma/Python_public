src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_C"

# ---- solution ----

from collections import deque

# ---- process ----

d = deque()
n = int(input())
for i in range(n):
    c = input().split()
    if c[0][0] == "i":
        d.appendleft(c[1])
    elif c[0] == "delete":
        try:
            d.remove(c[1])
        except ValueError:
            pass
    elif c[0][6] == "F":
        d.popleft()
    else:
        d.pop()
else:
    print(*d)
