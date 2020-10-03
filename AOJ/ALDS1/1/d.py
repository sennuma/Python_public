src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/1/ALDS1_1_D"


def mp(arr):
    maxv = arr[1] - arr[0]
    minv = arr[0]
    for i in range(1, len(arr)):
        maxv = max(maxv, arr[i] - minv)
        minv = min(minv, arr[i])
    return maxv


# ---- process ----
n = int(input())
r = []
for i in range(n):
    r.append(int(input()))
print(mp(r))
