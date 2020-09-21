from itertools import combinations as comb

data = []
while 1:
    n, x = map(int, input().split())
    if n == x == 0:
        break
    data.append([n, x, 0])

for d in data:
    nums = list(range(1, d[0] + 1))
    c = list(comb(nums, 3))
    for l in c:
        if sum(l) == d[1]:
            d[2] += 1

for d in data:
    print(d[2])

