src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/3/ALDS1_3_D"

# ---- solution ----


class Landscape:
    def __init__(self, data):
        pass


def grid(data, x, y):
    landscape = [[" " for i in range(x)] for i in range(y)]
    h = int(y / 2)
    for i in range(x):
        for j in data:
            if j == "\\":
                landscape[h][i] = "\\"
                h -= 1
            elif j == "/":
                landscape[h][i] = "/"
                h += 1
            else:
                landscape[h][i] = "_"

    return landscape


def show(a):
    for i in a:
        print(i)


# ---- process ----

pass
