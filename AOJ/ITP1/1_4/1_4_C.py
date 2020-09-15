def main():
    while True:
        stdin = input()
        a, op, b = int(stdin.split()[0]), stdin.split()[1], int(stdin.split()[2])
        if op == "?":
            break
        elif op == "+":
            print(a + b)
        elif op == "-":
            print(a - b)
        elif op == "*":
            print(a * b)
        elif op == "/":
            print(a // b)


if __name__ == "__main__":
    main()
