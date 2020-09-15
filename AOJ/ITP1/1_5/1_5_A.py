def main():
    data = []
    while True:  # Loading stdin
        h, w = [int(e) for e in input().split()]
        if h == w == 0:
            break
        else:
            data.append([h, w])

    for datum in data:
        line = "#" * datum[1]
        line = line + "\n"
        print(line * datum[0])


if __name__ == "__main__":
    main()
