def datacollector() -> list:
    data = list()
    while 1:
        m, f, r = map(int, input().split())
        if m == f == r == -1:
            break
        elif r == -1:
            r = 0
        data.append([m, f, r])
    return data


def evaluator(data: list) -> None:
    for d in data:
        if d[0] == -1 or d[1] == -1 or (sum(d[:2]) < 30 and d[2] < 30):
            print("F")
        elif sum(d[:2]) >= 80:
            print("A")
        elif sum(d[:2]) >= 65:
            print("B")
        elif sum(d[:2]) >= 50 or d[2] >= 50:
            print("C")
        elif sum(d[:2]) >= 30:
            print("D")
        else:
            print("F")


data = datacollector()
evaluator(data)
