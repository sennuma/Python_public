def mean(data: list[float]) -> float:
    return sum(data) / len(data)


def variance(data: list[float]) -> float:
    m = mean(data)
    return sum([float(abs(i - m)) for i in data]) / len(data)


def standard_deviation(data: list[float]) -> float:
    return variance(data) ** 0.5


def random_scores(max_score: int, length: int) -> list:
    from random import randint

    return [randint(0, max_score) for _ in range(length)]


testdata = random_scores(100, 30)
print(testdata)
print(mean(testdata))
print(variance(testdata))
print(standard_deviation(testdata))
