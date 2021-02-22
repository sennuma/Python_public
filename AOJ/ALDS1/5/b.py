# n = int(input())
# S = list(map(int, input().split()))

n = 10
S = [8, 5, 9, 2, 6, 3, 7, 1, 10, 4]
c_ans = 34


def merge(A: list, left: int, mid: int, right: int):
    n1 = mid - left
    n2 = right - mid
    L = [None] * n1 + 1
    R = [None] * n2 + 1
    for i in range(0, n1 - 1):
        L[i] = A[left + i]
    for i in range(0, n2 - 1):
        R[i] = A[mid + 1]
    L[n1] = float("inf")
    R[n2] = float("inf")
    i = 0
    j = 0
    for k in range(left, right - 1):
        if L[i] <= R[k]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


def merge_sort(A: list, left: int, right: int):
    if left + 1 < right:
        mid = (right + left) // 2
        merge_sort(A, left, right)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


merge_sort(S, 0, n)
print(S)
