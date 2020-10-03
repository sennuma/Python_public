src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_A"


def insertionsort(a):
    n = len(a)
    for i in range(1, n):
        v = a[i]
        j = i - 1
        print(*a)
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = v
    print(*a)


# ---- process ----

input()
insertionsort(list(map(int, input().split())))
