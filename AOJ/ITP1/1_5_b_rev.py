def lid(l: int):
    "print # of l-length"
    print("#" * l)


def wall(l: int):
    "print #, . of l-length-2, and # at rightmost"
    print("#" + "." * (l - 2) + "#")


def buildframe(size: tuple):
    "print frame with given size and a blank line under the frame"
    for i in range(size[0]):
        if i == 0 or i == size[0] - 1:
            lid(size[1])
        else:
            wall(size[1])
    print()  # for blank line


while 1:
    d = tuple(map(int, input().split()))
    if d[0] == d[1] == 0:
        break
    buildframe(d)
