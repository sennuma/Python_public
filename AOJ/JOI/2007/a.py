def main():
    price = int(input())
    num = 0
    coins = (500, 100, 50, 10, 5, 1)
    charge = 1000 - price
    for coin in coins:
        while charge >= coin:
            charge -= coin
            num += 1
    print(num)


if __name__ == "__main__":
    main()
