src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_B"
__test = 1

# ---- solution ----


def insertionsort(a):
    n = len(a)
    cnt = 0
    for i in range(n):  # 整列部分のインデックス
        minj = i
        for j in range(i, n):  # 非整列部分における最小値を探索
            if a[j] < a[minj]:
                minj = j
        a[i], a[minj] = a[minj], a[i]
        cnt += 1
    return cnt


# ---- process ----

if __test:
    a = [5, 6, 4, 2, 1, 3]
    c = insertionsort(a)
    print(*a)
    print(c)
    a = [5, 6, 4, 2, 1, 3]
else:
    input()
    a = list(map(int, input().split()))
    c = insertionsort(a)
    print(*a)
    print(c)
