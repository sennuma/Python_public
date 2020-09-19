def bldginfo(bldg: list) -> None:
    for i in range(4):
        for f in bldg[i]:
            for r in f:
                print(f" {r}", end="")
            else:
                print()
        if i != 3:
            print("####################")


# --------------
bldg = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n = int(input())  # number of info
b = int()  # bldg
f = int()  # floor
r = int()  # room
v = int()  # size of in/out

for i in range(n):
    b, f, r, v = map(int, input().split())
    bldg[b - 1][f - 1][r - 1] += v

bldginfo(bldg)
