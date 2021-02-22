def isloadable(pld, num_trucks, weights):
    trucks = [pld] * num_trucks
    n, i = 0, 0
    while i < len(weights):
        if trucks[n] - weights[i] < 0:
            n += 1
            if n == num_trucks:
                return False
        else:
            trucks[n] -= weights[i]
            i += 1
    return True


def calcpld(num_trucks, weights):
    l = max(weights)
    r = sum(weights)
    a = r
    while l <= r:
        m = (l + r) // 2
        if isloadable(m, num_trucks, weights):
            a = m
            r = m - 1
        else:
            l = m + 1
    return a


def sl_tuplizer(t):
    r = tuple(map(t, input().split()))
    return r


def ml_tuplizer(t, n):
    r = tuple((t(input()) for _ in range(n)))
    return r


def main():
    n, k = sl_tuplizer(int)
    w = ml_tuplizer(int, n)
    print(calcpld(k, w))


main()
