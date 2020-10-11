src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_B"

# ---- solution ----


class Queue:
    def __init__(self, data=[]):
        self.data = data

    def enqueue(self, x):
        self.data.append(x)

    def dequeue(self):
        x = self.data[0]
        self.data = self.data[1:]
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
q = Queue()
for i in range(n):
    j = input().split()
    j[1] = int(j[1])
    q.enqueue(j)

pt = 0
while not q.data == []:
    t = q.dequeue()
    r = donewithin(t, qt)
    if not r[0]:
        q.enqueue(r[1])
        pt += qt
    elif r[0]:
        pt += r[1]
        print(t[0], pt)
