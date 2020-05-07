# https://onlinejudge.u-aizu.ac.jp/courses/lesson/2/ITP1/3/ITP1_3_D


def main():
    a, b, c = (int(e) for e in input().split())
    cnt = 0
    for d in range(a, b+1):
        if c % d == 0:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
