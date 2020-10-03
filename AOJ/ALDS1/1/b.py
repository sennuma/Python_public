src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_B"


def gcd(x, y):
    if x < y:
        y, x = x, y
    while y > 0:
        r = x % y
        x = y
        y = r
    return x


# ---- process ----
x, y = tuple(map(int, input().split()))
print(gcd(x, y))
