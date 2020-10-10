src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_B"

# ---- solution ----

from collections import OrderedDict as odict


class Queue:
    def __init__(self, data=odict()):
        self.data = odict


# ---- process ----
__test = 1

if __test:
    stdin = """p1 150
p2 80
p3 200
p4 350
p5 20"""
    n, qt = tuple(map(int, "5 100".split()))
    d = odict()
    for i in stdin.split("\n"):
        s = i.split()
        d[s[0]] = int(s[1])

    q = Queue(d)
else:
    n, qt = tuple(map(int, input().split()))
    d = odict()
    for i in range(n):
        s = input().split()
        d[s[0]] = int(s[1])

    queue = Queue(d)
