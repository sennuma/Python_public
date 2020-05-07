def main():
    n = int(input())
    l = [int(e) for e in input().split()]
    print(min(l), max(l), sum(l))


if __name__ == "__main__":
    main()
