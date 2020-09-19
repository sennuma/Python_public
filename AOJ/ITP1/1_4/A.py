# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/4/ITP1_4_A


def main():
    a, b = (int(e) for e in input().split())
    d = int(a / b)
    r = a % b
    f = a / b
    print(f"{d} {r} {f:.5f}")


if __name__ == "__main__":
    main()
