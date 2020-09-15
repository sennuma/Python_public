def main(l, a) -> None:
    l = int(l)
    a = [i for i in reversed(a.split())]
    for i in a[:-1]:
        print(f"{i} ", end="")
    print(a[-1])


if __name__ == "__main__":
    main(l=input(), a=input())
