src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_B"
__test = 0

# ---- solution ----


def insertionsort(a) -> int:
    cnt = 0
    n = len(a)
    for i in range(n - 1):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j
        if i != minj:
            a[i], a[minj] = a[minj], a[i]
            cnt += 1
    return cnt


# ---- process ----

if __test:
    pass
else:
    input()
    a = list(map(int, input().split()))
    c = insertionsort(a)
    print(*a)
    print(c)
