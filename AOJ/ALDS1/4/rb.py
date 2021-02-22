def binarysearch(arr, key):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] > key:
            right = mid
        else:
            left = mid + 1
    return False


def main():
    input()
    s = tuple(map(int, input().split()))
    input()
    t = tuple(map(int, input().split()))
    c = 0
    for i in t:
        if binarysearch(s, i):
            c += 1
    print(c)


main()
