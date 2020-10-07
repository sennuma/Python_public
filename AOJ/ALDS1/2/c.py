src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2/ALDS1_2_C"

# ---- solution ----


def bubblesort(c) -> None:
    n = len(c)
    flag = 1
    while flag:
        flag = 0
        for j in range(n - 1, 0, -1):
            if c[j][1] < c[j - 1][1]:
                c[j], c[j - 1] = c[j - 1], c[j]
                flag = 1


def selectionsort(c) -> None:
    n = len(c)
    for i in range(n - 1):
        minj = i
        for j in range(i, n):
            if c[j][1] < c[minj][1]:
                minj = j
        c[i], c[minj] = c[minj], c[i]


# ---- process ----
__test = 0
if __test:
    cards = "H4 C9 S4 D2 C3".split()
    c1 = cards[:]
    c2 = cards[:]
    bubblesort(c1)
    print(*c1)
    print("Stable")  # cuz stable

    selectionsort(c2)
    print(*c2)
    print("Stable" if c1 == c2 else "Not stable")
else:
    input()
    cards = input().split()
    c1 = cards[:]
    c2 = cards[:]
    bubblesort(c1)
    print(*c1)
    print("Stable")  # cuz stable

    selectionsort(c2)
    print(*c2)
    print("Stable" if c1 == c2 else "Not stable")
