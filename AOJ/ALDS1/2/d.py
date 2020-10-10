src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_D"

# ---- solution ----


def insertionsort(a, g, c) -> int:
    """
    a ::= an array of the sorting target
    g ::= a distance for distanced insertion sort
    c ::= a variable for cnt

    returns c
    """
    cnt, n = c, len(a)
    for i in range(g, n):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j + g] = a[j]
            j = j - g
            cnt += 1
        a[j + g] = v
    return cnt


def shellsort(a) -> tuple:
    cnt, n = 0, len(a)
    g, h = [], 0
    while h <= n / 9:
        h = 3 * h + 1
        g.append(h)
    g = tuple(g)

    for i in reversed(g):
        cnt = insertionsort(a, i, cnt)
    return g, cnt


# ---- process ----

__test = 0
if __test:
    a = [5, 1, 4, 3, 2]
    g, c = shellsort(a)
    print(*reversed(g))
    print(c)
else:
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    g, c = shellsort(a)
    print(len(g))  # as m
    print(*reversed(g))
    print(c)
    for i in range(n):
        print(a[i])
