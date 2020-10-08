src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_D"

# ---- solution ----


def insertionsort(a, n, g):
    cnt = 0
    for i in range(g, n - 1):
        v = a[i]
        j = i - g
        while j >= 0 and a[j] > v:
            a[j + g] = a[j]
            j = j - g
            cnt += 1
        a[j + g] = v


def shellsort(a, n) -> int:
    cnt = 0
    m = 0
    g = ["?", "?", "...", "?"]
    for i in range(0, m - 1):
        insertionsort(a, n, g[i])


def t(a):
    l = len(a)
    h = 1
    while h < l / 9:
        h = h * 3 + 1
    while h > 0:
        for i in range(h, l):
            j = i
            while j >= h and a[j - h] > a[j]:
                a[j], a[j - h] = a[j - h], a[j]
                j -= h
        h = int(h / 3)


# ---- process ----

__test = 1
if __test:
    pass
else:
    n = int(input())
    A = [5, 1, 4, 3, 2]
    for i in range(n):
        A.append(int(input()))
    # print(int(m))
    # print(*G)
    # print(cnt)
    # for i in range(n):
    #     print(A[i])
