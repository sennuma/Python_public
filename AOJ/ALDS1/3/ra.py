src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_A"

# ---- solution ----

import queue


def rpn(*args):
    """
    reverse polish notation.
    """
    o1, o2 = int(args[0]), int(args[1])
    if args[2] == "+":
        return o2 + o1
    elif args[2] == "-":
        return o2 - o1
    elif args[2] == "*":
        return o2 * o1


operators = "+-*"

# ---- process ----

__test = 0
if __test:
    o = "1000 500 132 + 132 - 2 * 100 10 10 * + - 50 50 50 50 + + + + 10 999 * + 24 + + 24 - 10 * 15000 -".split()
    s = queue.LifoQueue()
    for i in o:
        if i not in operators:
            s.put(int(i))
        else:
            o1 = s.get()
            o2 = s.get()
            s.put(rpn(o1, o2, i))
    else:
        print(s.get())
else:
    o = input().split()
    s = queue.LifoQueue()
    for i in o:
        if i not in operators:
            s.put(int(i))
        else:
            o1 = s.get()
            o2 = s.get()
            s.put(rpn(o1, o2, i))
    else:
        print(s.get())
