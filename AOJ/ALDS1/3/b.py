src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_B"

# ---- solution ----


class Queue:
    def __init__(self, maxsize):
        """"""
        self.max = maxsize
        self.data = [[]] * maxsize
        self.t, self.h = 0, 0

    def isempty(self):
        """"""
        return self.t == self.h

    def isfull(self):
        """"""
        return self.h == (self.t + 1) % self.max

    def enqueue(self, x):
        """"""
        if self.isfull():
            raise IndexError("Overflow; queue is full")
        self.data[self.t] = x
        if self.t + 1 == self.max:
            self.t = 0
        else:
            self.t += 1

    def dequeue(self):
        """"""
        if self.isempty():
            raise IndexError("Underflow; queue is empty")
        x = self.data[self.h]
        if self.h + 1 == self.max:
            self.h = 0
        else:
            self.h += 1
        return x


def donewithin(tgt, qt) -> tuple:
    """check if task can be done within given qt
    return (True, processed time) or (False, [tgt[0], rrt])"""
    if tgt[1] <= qt:
        return (True, tgt[1])
    else:
        return (False, [tgt[0], tgt[1] - qt])


# ---- process ----

n, qt = tuple(map(int, input().split()))
q = Queue(n + 1)
for i in range(n):
    j = input().split()
    j[1] = int(j[1])
    q.enqueue(j)

pt = 0
while not q.data == []:
    try:
        t = q.dequeue()
    except IndexError:
        break
    r = donewithin(t, qt)
    if not r[0]:
        q.enqueue(r[1])
        pt += qt
    elif r[0]:
        pt += r[1]
        print(t[0], pt)
