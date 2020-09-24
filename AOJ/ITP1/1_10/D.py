src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/all/ITP1_10_D"


class Minkowski:
    def __init__(self, x: list, y: list):
        self.x = x
        self.y = y

    def distance(self, p: int) -> float:
        if p == 0:
            return max(abs(i - j) for i, j in zip(self.x, self.y))
        else:
            return (sum([(abs(i - j)) ** p for i, j in zip(self.x, self.y)])) ** (1 / p)


if __name__ == "__main__":
    input()
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    a = Minkowski(x, y)
    for i in range(1, 4):
        print("{:8f}".format(a.distance(i)))
    print("{:8f}".format(a.distance(0)))

