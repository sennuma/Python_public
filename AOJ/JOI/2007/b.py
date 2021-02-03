def main():
    s = input()
    jo = 0
    io = 0
    for i in range(len(s), 2, -1):
        if s[i - 2 : i] == "OI":
            if s[i - 3] == "J":
                jo += 1
            elif s[i - 3] == "I":
                io += 1
    print(jo)
    print(io)


if __name__ == "__main__":
    main()
