def liniarsearch(T, R):
    c = 0
    for target in T:
        if target in R:
            c += 1
    return c


input()
S = input().split()
input()
T = input().split()
print(liniarsearch(T, S))
