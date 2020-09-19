def cardclassifier(s, n) -> int:
    n = int(n)
    if s == "S":
        return n
    elif s == "H":
        return 13 + n
    elif s == "C":
        return 26 + n
    else:
        return 39 + n


def missingcardfinder(cards: list) -> list:
    cards.sort()
    missings = []
    for i in range(1, 53):
        if i not in cards:
            missings.append(i)
    return missings


def missingcardprinter(cards: list) -> None:
    cards.sort()
    for i in cards:
        if i > 39:
            print(f"D {i-39}")
        elif i > 26:
            print(f"C {i-26}")
        elif i > 13:
            print(f"H {i-13}")
        else:
            print(f"S {i}")


n = range(int(input()))
cards = []
for i in n:
    cards.append(cardclassifier(*input().split()))

cards = missingcardfinder(cards)
missingcardprinter(cards)
