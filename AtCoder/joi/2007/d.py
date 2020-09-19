def riffle(cards: list) -> None:
    f = list(cards[: int(cards.__len__() / 2)])
    b = list(cards[int(cards.__len__() / 2) :])
    cards.clear()
    for i, j in zip(f, b):
        cards.extend([i, j])


def cut(cards: list, s: int) -> list:
    f = list(cards[:s])
    b = list(cards[s:])
    cards.clear()
    cards.extend(b + f)


n = 2 * int(input())
cards = list(range(1, n + 1))
m = int(input())
for i in range(m):
    stdin = int(input())
    if stdin:
        cut(cards, stdin)
    else:
        riffle(cards)

for i in range(n):
    print(cards[i])
