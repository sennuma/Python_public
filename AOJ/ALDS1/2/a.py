src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_A"
__test = 0


def bubblesort(a):
    """just a bubble sort."""
    n = len(a)
    flag = 1
    cnt = 0
    while flag:
        flag = 0
        for j in range(n - 1, 0, -1):
            if a[j] < a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]  # swapped
                flag = 1
                cnt += 1
    return cnt


# ---- process ----
if __test:
    a = [5, 3, 2, 4, 1]
    b = bubblesort(a)
    print(*a)
    print(b)
else:
    input()
    a = list(map(int, input().split()))
    b = bubblesort(a)
    print(*a)
    print(b)

