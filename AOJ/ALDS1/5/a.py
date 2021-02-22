n = int(input())
A = list(map(int, input().split()))
q = int(input())
ms = list(map(int, input().split()))


def solve(i, m):
    if m == 0:
        return True
    if i >= n:
        return False
    if sum(A[i:]) < m:
        return False

    return solve(i + 1, m) or solve(i + 1, m - A[i])


for a in ms:
    print("yes" if solve(0, a) else "no")
