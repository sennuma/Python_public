# src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_B"


def bs(arr, qrys):
    cnt = 0
    for qry in qrys:
        left = 0
        right = len(arr)
        while left < right:
            pnt = (left + right) // 2
            if arr[pnt] == qry:
                cnt += 1
                break
            elif qry < arr[pnt]:
                right = pnt
            else:
                left = pnt + 1
    return cnt


input()
S = input().split()
input()
T = input().split()
c = bs(S, T)
print(c)
