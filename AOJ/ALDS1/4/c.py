d = dict()
for _ in range(int(input())):
    c, s = tuple(input().split())
    if c == "insert":
        d[s] = True
    elif d.get(s):
        print("yes")
    else:
        print("no")
