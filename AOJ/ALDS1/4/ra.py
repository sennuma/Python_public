# src = r"https://onlinejudge.u-aizu.ac.jp/courses/lesson/1/ALDS1/4/ALDS1_4_A"


def liniarsearch(targets, references):
    count = 0
    for target in targets:
        if target in references:
            count += 1
    return count


dev = 0
if dev:
    n = int("10")
    S = list(map(int, "10 9 8 7 6 5 4 3 2 1".split()))
    q = int("5")
    T = list(map(int, "11 12 13 14 15".split()))
else:
    n = int(input())
    S = list(map(int, input().split()))
    # n 個の整数を含む数列 S; len(S) == n
    q = int(input())
    T = list(map(int, input().split()))
    # q 個の異なる整数を含む数列 T; len(T) == q
    # T の要素は重複しない
    # T に含まれる整数の中で S に含まれるものの個数 C を出力する

C = liniarsearch(T, S)
print(C)
