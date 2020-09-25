src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/10/ITP1_10_C"


class ScoreSet:
    def __init__(self, scores):
        self.__scores = scores

    @property
    def scores(self) -> list:
        return self.__scores

    @property
    def mean(self) -> float:
        return sum(self.scores) / len(self.scores)

    @property
    def deviations(self) -> list:
        return [i - self.mean for i in self.scores]

    @property
    def dispersion(self) -> float:
        return sum([i ** 2 for i in self.deviations]) / len(self.scores)

    @property
    def stddeviation(self) -> float:
        return self.dispersion ** 0.5


if __name__ == "__main__":
    results = []
    while 1:
        n = int(input())
        if not n:
            break
        x = list(map(int, input().split()))
        x = ScoreSet(x)
        results.append(x.stddeviation)

    for r in results:
        print("{:6f}".format(r))
