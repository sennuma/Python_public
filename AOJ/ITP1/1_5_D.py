def checknum(x: int, i: int) -> bool:
    if x % 3 == 0:
        print(f" {x}", end="")
        return True
    return False


def include3(x: int, i: int) -> bool:
    if "3" in str(x):
        print(f" {x}", end="")
        return True
    return False


def main(n: int) -> None:
    for i in range(3, n + 1, 1):
        if not include3(i, n):
            checknum(i, n)
    print()


if __name__ == "__main__":
    main(n=int(input()))
