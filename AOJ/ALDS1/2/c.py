src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/2"
__test = 1

# ---- solution ----


def bubblesort(c):
    n = len(c)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            pass


def selectionsort():
    pass


# ---- process ----

if __test:
    cards = "H4 C9 S4 D2 C3".split()
    ss = [cards[i][0] for i in range(len(cards))]
    ns = [cards[i][1] for i in range(len(cards))]
else:
    input()
    cards = input().split()
    ss = [cards[i][0] for i in range(len(cards))]
    ns = [cards[i][1] for i in range(len(cards))]
